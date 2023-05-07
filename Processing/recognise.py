import csv
import numpy as np
import time
import Processing.readcsv as rcsv
import Processing.fingerprint as fp
import Processing.Window as window
import Processing.Similarity as sim
def result(fp):
    with open('fingerprint_db.csv', 'r') as csvFile:
        reader = list(csv.reader(csvFile))
    #Return list of list of fingerprint from csv
    s=rcsv.readlistfp(reader)
    # list
    resultcs=[]
    result=[]
    System_time1 = time.asctime(time.localtime(time.time()))
    print("\nAsctime function output:", System_time1)
    print(len(s))
    for i in range(len(s)):
        v=s[i]
        cosin=sim.cosine_Similarity(fp,v)
        resultcs.append([i,cosin])
    resultcs.sort(key = lambda x : x[1],reverse=True)
    
    for i in range(len(resultcs)):
        result.append([rcsv.get_value_from_index(resultcs[i][0]),resultcs[i][1]])
    return result
    
    
