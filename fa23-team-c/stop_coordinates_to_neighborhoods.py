import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

stops_df = pd.read_csv('data/stops_coordinates.csv')
neighborhoods_gdf = gpd.read_file('data/neighborhoods.geojson')

geometry = [Point(xy) for xy in zip(stops_df['longitude'], stops_df['latitude'])]
stops_gdf = gpd.GeoDataFrame(stops_df, crs='EPSG:4326', geometry=geometry)

stops_with_neighborhood = gpd.sjoin(stops_gdf, neighborhoods_gdf, how='left', predicate='within')
output_df = stops_with_neighborhood[['stop_id', 'neighborhood']]

output_df.to_csv('stops_to_neighborhoods.csv', index=False)