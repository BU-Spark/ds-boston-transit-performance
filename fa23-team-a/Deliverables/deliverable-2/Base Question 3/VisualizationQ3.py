import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import wkt
from google.colab import drive
import os
drive.mount('/content/MyDrive/')

dir_path = '/content/MyDrive/MyDrive/City of Boston: Transit & Performance A/Data Files/'
files = files = os.listdir(dir_path)

df = pd.read_pickle(f"{dir_path}/stop_info.pkl")
df = df.dropna()
df['geometry'] = df['geometry'].apply(lambda point: str(point))
df['geometry'] = df['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry='geometry')

world_cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
boston_map = world_cities[world_cities['name'] == 'Boston']
# Load Boston map


# Plotting
fig, ax = plt.subplots(figsize=(10, 10))


# Normalize the accuracy for color mapping
norm = plt.Normalize(gdf['accuracy'].min(), gdf['accuracy'].max())
cmap = plt.cm.RdYlGn_r

# Plot each point
for idx, row in gdf.iterrows():
    ax.scatter(row.geometry.x, row.geometry.y, 
               color=cmap(norm(row.accuracy)), 
               edgecolor='black',
               s=100) # arbitrary size

# Add color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm._A = []
plt.colorbar(sm, ax=ax, orientation='vertical', label='Accuracy')

# Set labels and title
ax.set_title('Bus Stops in Boston with Accuracy Indication')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()