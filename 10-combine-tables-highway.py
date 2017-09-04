import pandas as pd

inInt = 'data/processing/new_york_new_york_points_int_ct10.csv'
inTra = 'data/input/beh_nyc_walkability.csv'
inHig = 'data/processing/osm_highway_pivot.csv'
inTag = 'data/processing/osm_tags_pivot_cln.csv'

dfInt = pd.read_csv(inInt)
dfTra = pd.read_csv(inTra)
dfHig = pd.read_csv(inHig)
dfTag = pd.read_csv(inTag)

dfInt = dfInt[['geoid','osm_id']]
dfTra = dfTra[['geoid','t10walk','t10lndkm2']]

df = dfInt.merge(dfTra, how='left', on='geoid')
df = df.merge(dfHig, how='left', on='osm_id')
df = df.merge(dfTag, how='left', on='osm_id')

df_old = df

df = df.drop(['osm_id','gnis_created','gnis_county_id','gnis_state_id','capacity','addr_state','addr_city','religion'], axis=1)

dfStringCols = []

for i in df.columns:
	if df[i].dtype == 'object':
		dfStringCols.append(i)

df['index_col'] = df.index

colTotal = 0
for i in dfStringCols:
	print i
	one_hot = pd.get_dummies(df[i])
	colTotal = colTotal + len(one_hot.columns)
	one_hot = one_hot.rename(columns = lambda x : i + '_one_hot_' + x)
	one_hot['index_col'] = one_hot.index
	df = df.merge(one_hot, on='index_col', how='left')

df = df.drop(dfStringCols, axis=1)


df = df.groupby(['geoid','t10walk','t10lndkm2'],as_index=False).sum() # sum osm features to tract boundaries

df = df.fillna(0)


colsList = df.columns

for i in colsList:
	if i != 'geoid' and i != 'osm_id'  and i != 't10walk'  and i != 't10lndkm2':
		print i 
		df[i] = df[i]/df['t10lndkm2'] # get osm feature density by tract area

### GET A DENSITY OF AMENITIES AND NON_NUMERICAL DATA
### One hot before calculating densities... 


df = df.drop(['t10lndkm2','index_col'], axis=1)

df = df.fillna(0)

ouCSV = 'data/processing/walkability_highway_tags_features.csv'
df.to_csv(ouCSV, index=False)

