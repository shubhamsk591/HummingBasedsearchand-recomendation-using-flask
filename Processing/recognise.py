import csv
import numpy as np
import Processing.readcsv as rcsv
import Processing.fingerprint as fp
import Processing.Window as window
import Processing.Similarity as sim
def result(fp):
    with open('fingerprint_db.csv', 'r') as csvFile:
        reader = list(csv.reader(csvFile))
    #Return list of list of fingerprint from csv
    s=rcsv.readlistfp(reader)
    #Return X and Y separate for the list of list
    x1,y1=rcsv.fingerprintlist(s)
    x=np.array(fp[0])
    y=np.array(fp[1])
    resultcs=[]
    print("Spliting Data for Sliding")
    for i in range(len(x1)):
        tx=np.array(x1[i])
        ty=np.array(y1[i])
        splittx,splitty=window.slide(x,tx,ty)
        vectored=[]
        
        for r in range(len(splittx)):
            vectored.append(sim.cosine(splittx[r],x,splitty[r],y))
            
        resultcs.append(max(np.array(vectored)))
    
    output=[]
    result=[]
    print("Using Cosine Similarity")
    for j in range(len(resultcs)):
        output.append([j,resultcs[j]])
    output.sort(key = lambda x : x[1],reverse=True)
    for i in range(len(output)):
        result.append([rcsv.get_value_from_index(output[i][0],"fingerprint_db.csv"),output[i][1]])

    return result
    
    
