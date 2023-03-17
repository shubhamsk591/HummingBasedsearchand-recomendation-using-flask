import Processing.fingerprint as f
import os
import pandas as pd
# Get the list of all the song files in folder
song_files = os.listdir('static/Dataset_Songs/')

# Initialize the database
features_db = pd.DataFrame()

# Iterate over all the songs and extract the features
for file in song_files:
   print(file)
   file_name="static/Dataset_Songs/"+file
   features = f.fingerprint(file_name)
   n=len(features[0])
   val=[]
   val.append(file)
   val.append(n)

   for i in range(n):
      a=int(features[0][i])
      b=int(features[1][i])
      a=[a,b]
      val.append(a)
   df = pd.DataFrame([val])
   
   features_db = features_db.append(df, ignore_index = True)
features_db.to_csv('fingerprint_db.csv')