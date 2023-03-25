import librosa
import numpy as np
def normalized(a):
    a = (a - a.min()) / (a.max() - a.min())
    
    return a
#Defining the feature extraction function
def extract_features(file_name):
    # Load the audio file
    audio, sample_rate = librosa.load(file_name)
    val=[]
    #Extract mfcc feature 20 features
    mfcc=librosa.feature.mfcc(y=audio, sr=sample_rate)
    for x in range(len(mfcc)):
        v=normalized(mfcc[x])
        val.append(np.mean(v))
    #Extract Chroma Feature 
    chroma_frequencies = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
    for x in range(len(chroma_frequencies)):
        v=normalized(chroma_frequencies[x])
        val.append(np.mean(v))
    #Extract Spectral_Contrast
    spectral_contrast = librosa.feature.spectral_contrast(y=audio, sr=sample_rate)
    for x in range(len(spectral_contrast)):
        v=normalized(spectral_contrast[x])
        val.append(np.mean(v))
    #Extract Tones
    tonal_centroid_features = librosa.feature.tonnetz(y=audio, sr=sample_rate)
    for x in range(len(tonal_centroid_features)):
        v=normalized(tonal_centroid_features[x])
        val.append(np.mean(v))
    
    #Extract Spectral_Centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sample_rate)
    spectral_centroid=normalized(spectral_centroid)
    val.append(np.mean(spectral_centroid))
    #Zero Cross rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio)
    zero_crossing_rate=normalized(zero_crossing_rate)
    val.append(np.mean(zero_crossing_rate))
    # Extract beats per minutes
    tempo,beat = librosa.beat.beat_track(y=audio,sr=sample_rate)
    val.append(np.mean(beat))
    val.append(tempo)
    #return list
    return val
