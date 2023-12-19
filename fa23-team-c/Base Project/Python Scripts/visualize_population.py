import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# file_path_geojson = 'neighborhoods.geojson'
# gdf_neighborhoods = gpd.read_file(file_path_geojson)

# file_path_csv = 'census.csv'
# data = pd.read_csv(file_path_csv)

# merged_data = gdf_neighborhoods.merge(data, how='left', left_on='neighborhood', right_on='field concept')
# output_geojson_path = 'merged_data.geojson'
# merged_data.to_file(output_geojson_path, driver='GeoJSON')

# Load the GeoJSON file
data = gpd.read_file('merged_data.geojson')

# Create a dictionary to map neighborhood names to numbers
neighborhood_dict = {neighborhood: i + 1 for i, neighborhood in enumerate(data['neighborhood'])}

# Plotting
fig, ax = plt.subplots()

# Plot the data (population)
data.plot(column='Total:', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Add numbered labels for the neighborhoods
for idx, row in data.iterrows():
    ax.text(row.geometry.centroid.x, row.geometry.centroid.y, str(neighborhood_dict[row['neighborhood']]),
            ha='center', va='center', fontsize=8, color='black')

plt.title('Neighborhood Populations', fontsize=20)
plt.axis('off')

# Create a legend for neighborhood numbers
handles = []
for neighborhood, number in neighborhood_dict.items():
    handles.append(plt.Line2D([0], [0], marker='.', color='w', label=f'{number}: {neighborhood}',
                              markerfacecolor='black', markersize=8))

plt.legend(handles=handles, loc="center left", bbox_to_anchor=(-0.4, 0.5))
plt.show()