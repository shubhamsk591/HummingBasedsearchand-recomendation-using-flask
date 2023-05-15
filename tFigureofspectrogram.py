import librosa
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
data1s,sr1s=librosa.load('static/Dataset_Songs/So_Gaya_Yeh_Jahan__From__Bypass_Road___resampled.mp3')
specgram, freq,times= mlab.specgram(data1s, NFFT=2048, Fs=sr1s, noverlap=int(2048 / 2))
x=np.array(specgram)
y=np.array(freq)
z=np.array(times)
x1=[]
for i in range(50):
    x1.append(x[i][0:50])

y,z=np.meshgrid(y[0:50],z[0:50])

x=np.array(x1) 
# syntax for 3-D plotting
ax = plt.axes(projection='3d')
# syntax for plotting
ax.plot_surface(z,y,x[0:50],cmap='inferno')
ax.set_title('Spectogram of clip')
ax.set_xlabel("Time sec")
ax.set_ylabel("Frequency Hz")
ax.set_zlabel("Magnitude dB ")
plt.show()