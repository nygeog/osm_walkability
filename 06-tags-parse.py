import pandas as pd

inCSV = 'data/processing/osm_other_tags.csv'

df = pd.read_csv(inCSV)

tagList = df.values.tolist()

df_list = []

for h in tagList:
    bucket = []
    x = h[1].split('","')
    
    for i in x:
        z = i.split("=>")
        osm = []
        
        for j in z: 
            osm.append(j.replace('"','').replace(':','_'))
        bucket.append(osm)

    df = pd.DataFrame(data=[h[0]], columns=['osm_id'])
    
    for i in bucket:
        #print i
        df[i[0]] = i[1]

    #print df.head(10)
    df_list.append(df)

print '...concatinating...'
df = pd.concat(df_list)
df = df.set_index('osm_id')

df.to_csv('data/processing/osm_tags_pivot.csv')