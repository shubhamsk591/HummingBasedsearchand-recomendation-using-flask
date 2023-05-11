import numpy as np
import math
from numpy import linalg

def cosine_Similarity(x,y):
   x=np.array(x)
   y=np.array(y)
   cosine=np.dot(x,y)/(linalg.norm(x)*linalg.norm(y))
   return cosine
def equclidean(x,y):
   x=np.array(x)
   y=np.array(y)
   dist=linalg.norm(x-y)
   return dist
