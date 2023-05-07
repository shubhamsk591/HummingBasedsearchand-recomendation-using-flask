import Processing.fingerprint as f
import os
import pandas as pd
import time
# Get the list of all the song files in folder
song_files = os.listdir('static/Dataset_Songs/')

# Initialize the database
features_db = pd.DataFrame()
song_db=pd.DataFrame()
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
# Iterate over all the songs and extract the features
for file in song_files:
   print(file)
   file_name="static/Dataset_Songs/"+file
   features = f.fingerprint(file_name)
   n=len(features)
   val=[]
   val.append(file)
   df1 = pd.DataFrame([val])
   song_db=song_db.append(df1,ignore_index=True)
   val.append(n)

   for i in range(n):
      a=features[i]
      val.append(a)
   df = pd.DataFrame([val])
   
   features_db = features_db.append(df, ignore_index = True)
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
features_db.to_csv('fingerprint_db.csv')
song_db.to_csv('songs_db.csv')
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)