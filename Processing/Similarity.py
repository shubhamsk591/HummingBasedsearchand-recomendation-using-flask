import numpy as np
import math
from numpy import linalg
def euclidien_distance(x,x1,y,y1):
    sum=0
    n=len(x)
    for i in range(n):
        sum = math.sqrt(math.pow(x[i] - x1[i], 2) + math.pow(y[i] - y1[i], 2))
        sum=sum+sum
    return sum/n

def cosine(x,x1,y,y1):
  x=np.array(x)
  x1=np.array(x1)
  y=np.array(y)
  y1=np.array(y1)
   # calculate the dot product between two vectors
  dot_product = np.sum(x*x1) + np.sum(y*y1)
  
  # calculate the magnitude of x
  magnitude_x = np.sqrt(np.sum(np.square(x,dtype=np.longdouble)) + np.sum(np.square(y,dtype=np.longdouble)))
  
  # calculate the magnitude of y
  magnitude_y = np.sqrt(np.sum(np.square(x1,dtype=np.longdouble)) + np.sum(np.square(y1,dtype=np.longdouble)))
  
  # calculate the cosine distance
  cosine_distance = dot_product / (magnitude_x * magnitude_y)
  
  return cosine_distance
def cosine_Similarity(x,y):
   x=np.array(x)
   y=np.array(y)
   cosine=np.dot(x,y)/(linalg.norm(y)*linalg.norm(y))
   return cosine