import geopandas as gpd
import osmnx as ox
import geojson as gj
import ast

boundary_geojson = gpd.read_file('reprojected.geojson')
#print(bounding_geojson.head())


point = 47.22347, 8.81724
dist = 1000
buildings = ox.features_from_point(point, {'building': True, 'room': True, 'bench': True}, dist=dist)


buildings_save = buildings.map(lambda x: str(x) if isinstance(x, list) else x)

buildings_final = gpd.clip(buildings_save, boundary_geojson)

buildings_final.to_file("C:\\Users\\niklas.vogel\\Projects\\PythonProjects\\CM_getOSM_for_Geojson\\output.geojson", driver="GeoJSON")
print("hi")



#47.22347/8.81724 mid