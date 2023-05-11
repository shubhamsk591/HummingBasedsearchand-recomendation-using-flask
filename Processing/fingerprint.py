import numpy as np
import matplotlib.mlab as mlab
import librosa
def fingerprint(file_path):
    data,sr=librosa.load(file_path)
    #Spectrogram 
    specgram, freq,times= mlab.specgram(data, NFFT=2048, Fs=sr, noverlap=int(2048 / 2))
    k=15
    peaks_array = spectrogram_to_peaks(specgram,k)
    return peaks_array


def spectrogram_to_peaks(specgram,k):
    n=len(specgram)
    m=len(specgram[0])
    m=int(m/k)
    peaks=[]
    for i in range(n):
        for j in range(k-1):
            mean_arr = np.mean(specgram[i][j*m:j*m+m])
            peaks.append(mean_arr)
        mean_arr = np.mean(specgram[i][j*m+m:])
        peaks.append(mean_arr)
    return peaks

