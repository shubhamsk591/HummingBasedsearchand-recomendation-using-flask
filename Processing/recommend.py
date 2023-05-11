import csv
import numpy as np
import Processing.readcsv as rcsv
import Processing.Similarity as sim
def result(fp):
    with open('features_db.csv', 'r') as csvFile:
        reader = list(csv.reader(csvFile))
    #Return list of list of fingerprint from csv
    s=rcsv.readlistfe(reader)   
    t=rcsv.featurelist(s)
    resultcs=[]
    resulteq=[]
    for i in range(len(t)):
        resultcs.append(sim.cosine_Similarity(t[i],fp))
        resulteq.append(sim.equclidean(t[i],fp))

    output=[]
    result=[]
    print("Using Cosine Similarity")
    for j in range(len(resultcs)):
        output.append([j,resultcs[j],resulteq[j]])
    output.sort(key = lambda x : x[1],reverse=True)
    for i in range(len(output)):
        result.append([rcsv.get_value_from_index1(output[i][0]),round(output[i][1],2),round(output[i][2],2)])

    return result