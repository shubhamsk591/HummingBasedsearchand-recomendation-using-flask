import Processing.featureExtract as f
import os
import pandas as pd
import time
#method 1

# Get the list of all the song files in folder
song_files = os.listdir('static/Dataset_Songs/')

# Initialize the database
features_db = pd.DataFrame()
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
# Iterate over all the songs and extract the features
for file in song_files:
   print(file)
   file_name="static/Dataset_Songs/"+file
   features = f.extract_features(file_name)
   val=[]
   val.append(file)
   val.append(features)
   df = pd.DataFrame([val])
   
   features_db = features_db.append(df, ignore_index = True)
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)   
features_db.to_csv('features_db.csv')
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)