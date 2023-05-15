import eyed3

audiofile = eyed3.load("static/Dataset_Songs/Aadha_Main_Aadhi_Vo__The_Soul_Of_Bholaa___From__Bholaa___resampled.mp3")

sample_rate = audiofile.info.sample_freq
bit_depth = audiofile.info.bit_rate
no_of_channel = audiofile.info.mode

print("Sample Rate : ",sample_rate)
print("Bit Depth : ",bit_depth)
print("Number of Channels : ",no_of_channel)

import mutagen.mp3

#open the mp3 file
file = mutagen.mp3.MP3("static/Dataset_Songs/Aadha_Main_Aadhi_Vo__The_Soul_Of_Bholaa___From__Bholaa___resampled.mp3")

#get sample rate
sample_rate = file.info.sample_rate

#get bit depth
#bit_depth = file.info.bits_per_sample

#get no. of channels
channels = file.info.channels

#get bit rate
bit_rate = file.info.bitrate

#print the info
print("Sample Rate:",sample_rate)
#print("Bit Depth:",bit_depth)
print("No. of Channels:",channels)
print("Bit Rate:",bit_rate)