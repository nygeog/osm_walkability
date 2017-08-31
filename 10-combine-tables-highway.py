import pandas as pd

inInt = 'data/processing/new_york_new_york_points_int_ct10.csv'
inTra = 'data/input/beh_nyc_walkability.csv'
inHig = 'data/processing/osm_highway_pivot.csv'

dfInt = pd.read_csv(inInt)
dfTra = pd.read_csv(inTra)
dfHig = pd.read_csv(inHig)

dfInt = dfInt[['geoid','osm_id']]
dfTra = dfTra[['geoid','t10walk','t10lndkm2']]

df = dfInt.merge(dfTra, how='left', on='geoid')
df = df.merge(dfHig, how='left', on='osm_id')

df_old = df

df = df.drop(['osm_id'], axis=1)

df = df.groupby('geoid').sum() # sum osm features to tract boundaries

colsList = df.columns

for i in colsList:
	if i != 'geoid' and i != 'osm_id'  and i != 't10walk'  and i != 't10lndkm2':
		print i 
		df[i] = df[i]/df['t10lndkm2'] # get osm feature density by tract area

df = df.drop(['t10lndkm2'], axis=1)

df = df.fillna(0)

ouCSV = 'data/processing/walkability_highway_features.csv'
df.to_csv(ouCSV) #, index=False)

