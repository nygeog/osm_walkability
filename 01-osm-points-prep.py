import pandas as pd 

inCSV = 'data/input/new-york_new-york_points.csv'

df = pd.read_csv(inCSV)

df = df[['X','Y','osm_id']]

df.columns = ['longitude','latitude','osm_id'] #just delcare col names here

df.to_csv('data/processing/new-york_new-york_points.csv', index=False)