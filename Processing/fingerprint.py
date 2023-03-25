import numpy as np
from scipy import ndimage

import matplotlib.mlab as mlab
import librosa
import pandas as pd
def fingerprint(file_path):
    data,sr=librosa.load(file_path)
    #Spectrogram 
    specgram, freqs, times = mlab.specgram(data, NFFT=4096, Fs=sr, noverlap=int(4096 / 2))
    specgram[specgram == 0]=1e-6
    peaks_array = spectrogram_to_peaks(specgram, freqs, times)
    peaks_where = np.where(peaks_array)
    
    return peaks_where

#90% cutoff threshold to remove noise
def find_ninety_C_k(spec_gram):
    spec_gram = spec_gram[spec_gram != 0] #remove 0's
    specgram_flattened = spec_gram.flatten() #returns copy of orig
    #natural log
    specgram_sorted = np.sort(np.log(np.abs(specgram_flattened)))
    specgram_length = len(specgram_sorted)

    ninety_index = int(0.9 * specgram_length)
    ninety_C_k = specgram_sorted[ninety_index]
    return ninety_C_k


def spectrogram_to_peaks(specgram, freqs, times):
    #creating filters
    fp = ndimage.generate_binary_structure(2,1)
    fp = ndimage.iterate_structure(fp, 20)
    #set thresholds 90th percentile
    background_threshold = find_ninety_C_k(specgram)
    peaks = ((specgram == ndimage.maximum_filter(specgram, footprint = fp) ) & (specgram > background_threshold))
    return peaks

