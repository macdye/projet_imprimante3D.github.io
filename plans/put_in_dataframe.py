from execution_of_scrap import *
import pandas as pd 
import numpy as np

df = pd.DataFrame(list_object)
df.id = pd.to_numeric(df.id, errors='coerce').fillna(0).astype(np.int64)
df = df.fillna('Not Find')

#retrer des données non pertirnante en g
del df[df.columns[-1]]
del df['is_manufacturable']
del df['manufacturable_price']
del df['visibility']
del df['featured']
del df['license_store']
del df['status']
del df['visits']
del df['position']
del df['price']
df = df.rename(columns={'id': 'object_id', 'folderURL' : 'folder_url'})

print(df)
