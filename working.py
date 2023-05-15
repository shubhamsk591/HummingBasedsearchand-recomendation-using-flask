import pandas as pd
import numpy as np
def get_value_from_index(index,csvfiler): 
   df = pd.read_csv(csvfiler)
   # return the value from the specified index 
   return df.iloc[index,1]
print(get_value_from_index(15,"features_db.csv"))