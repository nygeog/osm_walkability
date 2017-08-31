CREATE TABLE new_york_new_york_points_int_ct10 AS SELECT geoid.ct10, osm_id.new_york_new_york_points, latitude.new_york_new_york_points, longitude.new_york_new_york_points FROM ct10, new_york_new_york_points WHERE ST_INTERSECTS(ct10.the_geom, new_york_new_york_points.the_geom)


CREATE TABLE new_york_new_york_points_int_ct10_v2 AS (SELECT geoid, osm_id, latitude, longitude FROM ct10, new_york_new_york_points WHERE ST_INTERSECTS(ct10.the_geom, new_york_new_york_points.the_geom))

-- CartoDBfy
SELECT cdb_cartodbfytable('new_york_new_york_points_int_ct10')
SELECT cdb_cartodbfytable('new_york_new_york_points_int_ct10_v2')

-- Overviews