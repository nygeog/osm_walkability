import urllib
from _settings import *

url = 'https://dms2203.cartodb.com/api/v2/sql?filename=beh_walkability_ct2010.csv&format=csv&q=SELECT geoid,t10km2,t10lndkm2,t10cnt,t10resdn1,t10intden,t10entrpy,t10rtlfar,t10sub07d,t10walk,t10walkc,the_geom FROM ct10'

dl_file = urllib.URLopener()
dl_file.retrieve(url, INPUT_FOLDER+'/beh_nyc_walkability.csv')

url = 'https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf'

dl_file = urllib.URLopener()
dl_file.retrieve(url, INPUT_FOLDER+'/new-york_new-york.osm.pbf')

# https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm2pgsql-shapefiles.zip
# https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.imposm-shapefiles.zip
# https://mapzen.com/data/metro-extracts/metro/new-york_new-york/
# https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf
# ^ opened this in QGIS and saved as CSV
