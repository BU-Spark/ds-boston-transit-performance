import geopandas as gpd
import pandas as pd

zipcodes_gdf = gpd.read_file('data/ZIP_Codes.geojson')
neighborhoods_gdf = gpd.read_file('data/neighborhoods.geojson')

neighborhoods_with_zipcodes = []

for idx, neighborhood in neighborhoods_gdf.iterrows():
    neighborhood_polygon = neighborhood['geometry']
    intersecting_zipcodes = zipcodes_gdf[zipcodes_gdf.intersects(neighborhood_polygon)]
    zipcodes_in_neighborhood = set(intersecting_zipcodes['ZIP5'].tolist())
    
    neighborhood_name = neighborhood['neighborhood']
    neighborhoods_with_zipcodes.append({'Neighborhood': neighborhood_name, 'ZipCodes': ', '.join(map(str, zipcodes_in_neighborhood))})

result_df = pd.DataFrame(neighborhoods_with_zipcodes)
result_df.to_csv('neighborhoods_to_zipcodes.csv', index=False)