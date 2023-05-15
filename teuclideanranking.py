import time
import Processing.fingerprint as fp
import csv
import numpy as np
import time
import Processing.readcsv as rcsv
import Processing.Similarity as sim
def result(fp):
    with open('fingerprint_db.csv', 'r') as csvFile:
        reader = list(csv.reader(csvFile))
    #Return list of list of fingerprint from csv
    s=rcsv.readlistfp(reader)
    # list
    resultes=[]
    result=[]
    System_time1 = time.asctime(time.localtime(time.time()))
    print("\nAsctime function output:", System_time1)
    print(len(s))
    for i in range(len(s)):
        dist=sim.equclidean(s[i],fp)
        resultes.append([i,dist])
    resultes.sort(key = lambda x : x[1])
    
    for i in range(len(resultes)):
        result.append([rcsv.get_value_from_index(resultes[i][0]),round(resultes[i][1],2)])
    return result
    
    

System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
#Test audio/1m song.wav
fp1=fp.fingerprint("test_data/audio.wav")
print("Fingerprint Completed")
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
list=result(fp1)
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
for i in range(len(list)):
        print(i+1," ",list[i][0]," ",list[i][1])