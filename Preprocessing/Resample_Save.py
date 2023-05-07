import os
import Resample
song_files = os.listdir('E:\Songs/')
for file in song_files:
    file_name="E:\Songs/"+file
    Resample.resample(file_name,file)
