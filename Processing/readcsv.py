import ast
import pandas as pd


#Read from fingerprint csv
def readlistfp(reader):
    n=len(reader)
    listh=[]
    for i in range(1,n):
        #get size of the vector 
        t=int(reader[i][2])
        list=[]
        for j in range(3,t+3):
            list.append(float(reader[i][j]))
        listh.append(list)
    #return list of vectors 
    return listh



#locate song lane
def get_value_from_index(index): 
   df = pd.read_csv("songs_db.csv")
   # return the value from the specified index 
   return df.iloc[index,1]

def get_value_from_index1(index): 
   df = pd.read_csv("features_db.csv")
   # return the value from the specified index 
   return df.iloc[index,1]

#Read from features csv
def readlistfe(a):
    n=len(a)
    listh=[]
    for i in range(1,n):
        listh.append(a[i])
    return listh
def featurelist(list1):
    n=len(list1)
    sl=[]
    for i in range(n):
        s=ast.literal_eval(list1[i][2])
        sl.append(s)
    return sl

     