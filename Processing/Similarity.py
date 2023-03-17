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
import math 
def cosine(x,x1,y,y1):
  x=np.array(x)
  x1=np.array(x1)
  y=np.array(y)
  y1=np.array(y1)
  # calculate the dot product between two vectors
  dot_product = 0
  for i in range(len(x)):
     dot_product += x[i]*x1[i]
  for i in range(len(y)):
     dot_product += y[i]*y1[i]
  
   # calculate the magnitude of x
  sum_of_squaresx=np.sum(np.square(x))
  sum_of_squaresy=np.sum(np.square(y))
  sum1 = math.fsum([sum_of_squaresx, sum_of_squaresy])
  if(sum1>0):
     magnitude_x = math.sqrt(sum1)
  else:
     sum1=sum1*-1
     magnitude_x = math.sqrt(sum1)

  
   # calculate the magnitude of y
  sum_of_squaresx=np.sum(np.square(x1))
  sum_of_squaresy=np.sum(np.square(y1))
  sum1 = math.fsum([sum_of_squaresx,sum_of_squaresy])
  if(sum1>0):
     magnitude_y = math.sqrt(sum1)
  else:
     sum1=sum1*-1
     magnitude_y = math.sqrt(sum1)
  
  
   # calculate the cosine distance
  cosine_distance = dot_product / (magnitude_x * magnitude_y)
  if cosine_distance > 1:
      cosine_distance = 1.0
  
  return cosine_distance
def cosine_Similarity(x,y):
   x=np.array(x)
   y=np.array(y)
   cosine=np.dot(x,y)/(linalg.norm(y)*linalg.norm(y))
   return cosine