import numpy as np
import matplotlib.mlab as mlab
import librosa
def fingerprint(file_path):
    data,sr=librosa.load(file_path)
    #Spectrogram 
    specgram= mlab.specgram(data, NFFT=2048, Fs=sr, noverlap=int(2048 / 2))
    k=15
    peaks_array = spectrogram_to_peaks(specgram,k)
    return peaks_array


def spectrogram_to_peaks(specgram,k):
    n=int(len(specgram[0])/k)
    peaks=[]
    for i in range(n):
        mean_arr = np.mean(specgram[0][i*k:(i*k)+k])
        peaks.append(mean_arr)
    mean_arr=np.mean(specgram[0][(n-1)*k:])
    peaks.append(mean_arr)
    return peaks

