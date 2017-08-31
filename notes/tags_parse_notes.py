import pandas as pd

x = """addr:street""=>""Courtlandt Avenue"",""addr:postcode""=>""10451"",""addr:housenumber""=>""607"""

y = x.split(",")

dfAll = pd.DataFrame()

# for i in y:
# 	df = pd.DataFrame()
# 	z = i.split("=>")#.replace('""','')
# 	#print z[0], z[1]
# 	df[z[0].replace('""','')] = [z[1].replace('""','') for n in range(1)]
# 	print df.head()
# 	dfAll.append(df)

bucket = []

for i in y:
	z = i.split("=>")
	osm = []
	for j in z: 
		osm.append(j.replace('""','').replace(':','_'))
		
	bucket.append(osm)

df = pd.DataFrame(data=[0])

for i in bucket:
	df[i[0]] = i[1]

df.head(10)


	#for j in z:
		#print j.replace('""','')