from shapely.geometry import shape
import osmnx as ox
import json

OUTPUT_FILE_NAME = "output.geojson"
BOUNDARY_FILE_NAME = "boundary.geojson"
RELEVANT_TAGS = {'building': True, 'room': True, 'door': True, 'indoor': True, 'amenity': True, 'sport': True, 'tourism': True, 'fauntain': True, 'leisure': True}
# turning of cache
ox.settings.use_cache = False

# makeig a polygon from the boundary file
with open(BOUNDARY_FILE_NAME) as f:
    features = json.load(f)["features"]

boundaries = shape(features[0]["geometry"])

# getting the data from osm
data_for_map = ox.features.features_from_polygon(boundaries, RELEVANT_TAGS)
map_geodataframe = data_for_map.map(lambda x: str(x) if isinstance(x, list) else x)


map_geodataframe.to_file(OUTPUT_FILE_NAME, driver="GeoJSON", na="drop")

# getting geojson to edit
with open(OUTPUT_FILE_NAME, 'r') as geojson_file:
    my_geojson = json.load(geojson_file)

# editing goejson date to delete None objects and changing osmid to @id and id
for feature in my_geojson["features"]:
    feat_props = feature["properties"]
    keys_to_delete = []

    for key, attrValue in feat_props.items():
        if not attrValue:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del feat_props[key]

    element_type = str(feat_props["element_type"])
    osm_id = str(feat_props["osmid"])
    id = f"{element_type}/{osm_id}"

    feat_props["@id"] = id
    feature['id'] = id

# saving edited geojson
with open(OUTPUT_FILE_NAME, 'w') as output_geojson_file:
    json.dump(my_geojson, output_geojson_file, indent=2, ensure_ascii=False)
