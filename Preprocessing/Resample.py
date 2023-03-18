from pydub import AudioSegment
import os

def resample(file_path,file):
    song = AudioSegment.from_mp3(file_path)

    resampled_song = song.set_frame_rate(22050)

    resampled_song.export(os.path.splitext("static/Dataset_Songs/"+file)[0] + '_resampled.mp3', format='mp3')