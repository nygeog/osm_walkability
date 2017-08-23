
# node[amenity=restaurant](-73.9442,40.6846,-73.9370,40.6898);

import overpass
api = overpass.API()
api = overpass.API(timeout=600)

response = api.Get('node["amenity"="restaurant"](40.62835018325247,-73.97480964660645,40.67074359544523,-73.9281177520752)')

response = api.Get('node(40.62835018325247,-73.97480964660645,40.67074359544523,-73.9281177520752)')

# NYC Bounds
# -74.2589, 40.4774, -73.7004, 40.9176
# 40.4774,-73.7004,40.9176,-74.2589

response = api.Get('node["amenity"="cafe"](40.4774,-73.7004,40.9176,-74.2589)')
response = api.Get('node["amenity"="cafe"](40.4774,-73.7004,40.9176,-74.2589)', responseformat="geojson")



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



dfb = df[(df.barriers == 'NY') 