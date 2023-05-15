import os
import pandas as pd
import time
import numpy as np
import matplotlib.mlab as mlab
import librosa
def fingerprint(file_path):
    data,sr=librosa.load(file_path)
    #Spectrogram 
    specgram, freq,times= mlab.specgram(data, NFFT=2048, Fs=sr, noverlap=int(2048 / 2))
    k=16
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


# Get the list of all the song files in folder
song_files = os.listdir('static/Dataset_Songs/')

# Initialize the database
features_db = pd.DataFrame()
song_db=pd.DataFrame()
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
# Iterate over all the songs and extract the features
for file in song_files:
   print(file)
   file_name="static/Dataset_Songs/"+file
   features = fingerprint(file_name)
   n=len(features)
   val=[]
   val.append(file)
   val.append(n)
   for i in range(n):
      a=features[i]
      val.append(a)
   df = pd.DataFrame([val])
   
   features_db = features_db.append(df, ignore_index = True)
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
features_db.to_csv('fingerprint_db_16.csv')
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)