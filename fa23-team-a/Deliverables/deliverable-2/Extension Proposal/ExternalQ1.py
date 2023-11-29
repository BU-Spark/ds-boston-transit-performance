import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.cluster import KMeans
import os
from google.colab import drive
drive.mount('/content/MyDrive/')

dir_path = '/content/MyDrive/MyDrive/City of Boston: Transit & Performance A/Data Files/'
files = files = os.listdir(dir_path)
columns = ['X', 'Y', 'stop_id', 'Routes']
df = pd.read_csv(f"{dir_path}/MBTA_Bus_Rapid_Transit_Reliability.csv", usecols=columns)

routes_array = df['Routes'].to_numpy()
def process_element(element):
    if isinstance(element, float):
        return 0
    else:
        # Count the number of '|' characters and add 1
        return element.count('|') + 1

# Assuming routes_array is the array you have from the DataFrame
mapped_array = [process_element(element) for element in routes_array]
mapped_array_reshaped = np.array(mapped_array).reshape(-1, 1)

# Creating a KMeans instance with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fitting the model and predicting the clusters
clusters = kmeans.fit_predict(mapped_array_reshaped)
print(clusters)
df['mapped_value'] = mapped_array
df['Cluster'] = clusters

cluster_averages = df.groupby('Cluster')['mapped_value'].mean()

# Sorting the cluster averages to get the order
sorted_cluster_indices = cluster_averages.sort_values().index

# Mapping the old cluster numbers to new ones based on the sorted order
cluster_mapping = {old_cluster: new_cluster for new_cluster, old_cluster in enumerate(sorted_cluster_indices)}

# Updating the cluster numbers in the DataFrame
df['Cluster'] = df['Cluster'].map(cluster_mapping)



gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['X'], df['Y']))

# Plotting each point, color-coded by the 'Cluster' column
fig, ax = plt.subplots()
colors = ['blue', 'green', 'red']  # Colors for each cluster

for cluster in range(3):
    # Filtering points in each cluster and plotting them in the respective color
    gdf[gdf['Cluster'] == cluster].plot(ax=ax, color=colors[cluster], label=f'BusyLevel {cluster}', markersize=7)

# Adding legend and axis labels
ax.legend()
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Clusters on Map')

plt.show()

df["Neighbor"] = pd.read_csv(file_path, usecols=["Neighborhood"])

neighbor_counts = df.groupby('Neighbor').size()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
neighbor_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Station by Neighborhood')
plt.xlabel('Neighbor')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotating the x-axis labels for better readability
plt.show()

def process_route_element(element):
    if isinstance(element, float):
        # If the element is a float, change it to 0
        return ["0"]
    else:
        # If the element is a string
        if '|' in element:
            # Split the string by '|' and convert to an array of integers
            return [num for num in element.split('|') if num]
        else:
            # If the string does not contain '|', convert it directly to an integer
            return [element]

# Applying the processing to the 'Routes' column
routes_processed = df['Routes'].apply(process_route_element)

# Converting the processed data into a list (array)
routes_array = routes_processed.tolist()

df["Route_Process"]=routes_array

def count_unique_routes(group):
    all_routes = sum(group['Route_Process'].tolist(), [])
    return len(set(all_routes))

count_route_by_neighbor = df.groupby('Neighbor').apply(count_unique_routes)

# Creating a bar chart for these counts
plt.figure(figsize=(10, 6))
count_route_by_neighbor.plot(kind='bar', color='green')
plt.title('Count of Unique Routes by Neighborhood')
plt.xlabel('Neighbor')
plt.ylabel('Count_Route')
plt.xticks(rotation=45)
plt.show()