import time
import Processing.fingerprint as fp
import Processing.recognise as final

System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
#Test audio/1m song.wav
fp1=fp.fingerprint("test_data/audio.wav")
print("Fingerprint Completed")
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
list=final.result(fp1)
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
for i in range(len(list)):
        print(i+1," ",list[i][0]," ",list[i][1])