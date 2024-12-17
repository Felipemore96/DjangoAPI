import geopandas as gpd
import requests

GEOJSON_FILE = './data/municipalities_nl.geojson'
API_URL = 'http://127.0.0.1:8000/api/features/'

# Read GeoJSON file w/ GeoPandas
gdf = gpd.read_file(GEOJSON_FILE)

# Loop through GeoDataFrame and post it to the API
for _, row in gdf.iterrows():
    data = {
        "name": row['name'],
        "geom": row['geometry'].__geo_interface__  # Convert geometry to GeoJSON **
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print(f"Successfully added: {row['name']}")
    else:
        print(f"Failed to add: {row['name']}, Error: {response.text}")

print("Data loading completed!")
