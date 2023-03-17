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
    for i in range(len(t)):
        resultcs.append(sim.cosine_Similarity(fp,t[i]))
    output=[]
    result=[]
    print("Using Cosine Similarity")
    for j in range(len(resultcs)):
        output.append([j,resultcs[j]])
    output.sort(key = lambda x : x[1],reverse=True)
    for i in range(len(output)):
        result.append([rcsv.get_value_from_index(output[i][0],"features_db.csv"),output[i][1]])

    return result