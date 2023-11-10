from shapely.geometry import shape
import osmnx as ox
import json

# turning of cache
ox.settings.use_cache=False

# makeig a polygon from the boundary file
with open("boundary.geojson") as f:
  features = json.load(f)["features"]

boundaries = shape(features[0]["geometry"])

# getting the data from osm
data_semi_final = ox.features.features_from_polygon(boundaries,
                                        {'building': True, 'room': True, 'door': True, 'indoor': True, 'amenity': True,
                                        'sport': True, 'tourism': True, 'fauntain': True, 'leisure': True})

map_final = data_semi_final.map(lambda x: str(x) if isinstance(x, list) else x)

# writing data to geojson
map_final.to_file("output.geojson", driver="GeoJSON")

# getting geojson to edit
geojson_file_path = 'output.geojson'
with open(geojson_file_path, 'r') as geojson_file:
    myGeoJSON = json.load(geojson_file)

# editing goejson date to delete None objects and changing osmid to @id and id
for feature in myGeoJSON["features"]:
    obj = feature["properties"]
    keys_to_delete = []
    idvalue = ""
    typevalue = ""
    for key, attrValue in obj.items():
        if not attrValue:
            keys_to_delete.append(key)
        if key == "element_type":
            typevalue = attrValue
        if key == "osmid":
            idvalue = attrValue
    for key in keys_to_delete:
        del obj[key]
    obj["@id"] = typevalue + "/" + str(idvalue)
    feature['id'] = typevalue + "/" + str(idvalue)

# saving edited geojson
with open(geojson_file_path, 'w') as output_geojson_file:
    json.dump(myGeoJSON, output_geojson_file, indent=2, ensure_ascii=False)
