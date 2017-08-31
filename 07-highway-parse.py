import pandas as pd
import numpy as np

inCSV = 'data/processing/osm_highway.csv'

df = pd.read_csv(inCSV)

df['count'] = 1

dfp = pd.pivot_table(df, values='count', index='osm_id',columns='highway', aggfunc=np.sum)

dfp = dfp.rename(columns=lambda x: x.replace(';', '_'))

ouCSV = 'data/processing/osm_highway_pivot.csv'

dfp.to_csv(ouCSV)