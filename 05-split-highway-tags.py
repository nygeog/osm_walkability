import pandas as pd
import numpy as np

inCSV = 'data/input/new-york_new-york_points.csv'

df = pd.read_csv(inCSV)

dfH = df[['osm_id','highway']]
dfT = df[['osm_id','other_tags']]

dfH = dfH.dropna(subset=['highway'])

ouCSV = 'data/processing/osm_highway.csv'
dfH.to_csv(ouCSV, index=False)

dfT = dfT.dropna(subset=['other_tags'])

ouCSV = 'data/processing/osm_other_tags.csv'
dfT.to_csv(ouCSV, index=False)