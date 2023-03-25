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
            list.append(reader[i][j])
        listh.append(list)
    #return list of vectors [[[1,2],[1,4]],[[1,2],[1,4]]]
    return listh

def fingerprintlist(s):
    x1=[]
    y1=[]
    for i in range(len(s)):
        n=len(s[i])
        x=[]
        y=[]
        for j in range(n):
            #separate list as x and y
            len1=ast.literal_eval(s[i][j])
            x.append(int(len1[0]))
            y.append(int(len1[1]))
        x1.append(x)
        y1.append(y)
    return x1,y1

#locate song lane
def get_value_from_index(index): 
   df = pd.read_csv("songs_db.csv")
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

     