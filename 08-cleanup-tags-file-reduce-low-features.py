import pandas as pd
import numpy as np

inCSV = 'data/processing/osm_tags_pivot.csv'

df = pd.read_csv(inCSV)

dfLen = len(df.index)

keeperCols = []

for i in df.columns:
    countNulls = df[i].isnull().sum()
    pctNull = countNulls/(dfLen * 1.0)
    if df[i].nunique() < 500:
        if pctNull < 0.99:
            print i, pctNull, df[i].nunique()
            keeperCols.append(i)

keeperCols     
    
df = df[keeperCols+['osm_id']]        

ouCSV = 'data/processing/osm_tags_pivot_cln.csv'

df.to_csv(ouCSV, index=False)


# print pctNull, i, df[i].nunique()
# print df[i].unique()


#count unique values relative to nonNulls


#print df('leisure').nunique()
