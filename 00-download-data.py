import urllib
from _settings import *

url = 'https://dms2203.cartodb.com/api/v2/sql?filename=beh_walkability_ct2010.csv&format=csv&q=SELECT geoid,t10km2,t10lndkm2,t10cnt,t10resdn1,t10intden,t10entrpy,t10rtlfar,t10sub07d,t10walk,t10walkc,the_geom FROM ct10'

dl_file = urllib.URLopener()
dl_file.retrieve(url, INPUT_FOLDER+'/beh_nyc_walkability.csv')




# https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm2pgsql-shapefiles.zip
# https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.imposm-shapefiles.zip

# https://mapzen.com/data/metro-extracts/metro/new-york_new-york/

# https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf

# node[amenity=restaurant](-73.9442,40.6846,-73.9370,40.6898);

# response = api.Get('node["amenity"="restaurant"](40.62835018325247,-73.97480964660645,40.67074359544523,-73.9281177520752)')

# /*
# This is an example Overpass query.
# Try it out by pressing the Run button above!
# You can find more examples with the Load tool.
# */
# node
#   [amenity=restaurant]
#   ({{bbox}});
# out;

# /*
# This is an example Overpass query.
# Try it out by pressing the Run button above!
# You can find more examples with the Load tool.
# */
# node
#   [amenity=restaurant]
#   (40.62835018325247,-73.97480964660645,40.67074359544523,-73.9281177520752);
# out;