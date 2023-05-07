import numpy as np

def split(x,tx,ty):
    
    n1=int(len(tx)/len(x))
    x1=[[0]*len(x)]*n1
    y1=[[0]*len(x)]*n1
    x1= np.array(x1)
    y1= np.array(y1)
    c1=0
    for i in range(n1):
        for j in range(len(x)):
            x1[i][j]=tx[c1]
            y1[i][j]=ty[c1]
            c1=c1+1
    return x1,y1

def slide(x,tx,ty):
    tx=np.array(tx)
    ty=np.array(ty)
    
    n1=len(tx)-len(x)+1
    x1=np.array([[tx[i+j] for j in range(len(x))] for i in range(n1)])
    y1=np.array([[ty[i+j] for j in range(len(x))] for i in range(n1)])
    return x1,y1
'''
    n1=len(tx)-len(x)
    n1=n1+1
    x1=[[0.0]*len(x)]*n1
    y1=[[0.0]*len(x)]*n1
    x1= np.array(x1)
    y1= np.array(y1)
    for i in range(n1):
        c1=i
        for j in range(len(x)):
            x1[i][j]=tx[c1]
            y1[i][j]=ty[c1]
            c1=c1+1
    return x1,y1
    '''