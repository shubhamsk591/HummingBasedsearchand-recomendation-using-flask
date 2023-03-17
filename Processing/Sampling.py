from pydub import AudioSegment
import os

def resample(file_path,file,destination):
    song = AudioSegment.from_mp3(file_path)

    resampled_song = song.set_frame_rate(44100)

    resampled_song.export(os.path.splitext(destination+file)[0] + '_resampled.mp3', format='mp3')


