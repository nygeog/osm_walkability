import urllib
from _settings import *

url = 'https://dms2203.cartodb.com/api/v2/sql?filename=new_york_new_york_points_int_ct10_v2.csv&format=csv&q=SELECT geoid, osm_id, latitude, longitude FROM new_york_new_york_points_int_ct10_v2'

dl_file = urllib.URLopener()
dl_file.retrieve(url, PROCESSING_FOLDER+'/new_york_new_york_points_int_ct10.csv')
