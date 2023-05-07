from pydub import AudioSegment
import os
import wave
import pydub

def resample(file_path,file):
    #load from mp3
    sound = pydub.AudioSegment.from_mp3(file_path)
    #set sample rate 
    sound = sound.set_frame_rate(11025) 
    #set sample width
    sound = sound.set_sample_width(1)
    #set channel 
    sound = sound.set_channels(1)
    sound.export(os.path.splitext("static/Dataset_Songs/"+file)[0] + '_resampled.mp3', format='mp3')