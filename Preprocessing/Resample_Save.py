import os
import Resample
song_files = os.listdir('Song_database/')
for file in song_files:
    file_name="Song_database/"+file
    Resample.resample(file_name,file)
