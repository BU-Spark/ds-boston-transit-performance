import pandas as pd
import matplotlib.pyplot as plt

# Load the data for September 2022 and January 2022
september_data = pd.read_csv('202209-bluebikes-tripdata.csv')
january_data = pd.read_csv('202201-bluebikes-tripdata.csv')
# Load station data
stations_data = pd.read_csv('current_bluebikes_stations.csv')



# Calculate the total number of rides for each month
total_rides_september = len(september_data)
total_rides_january = len(january_data)

# Print out the comparison
print("Total rides in September 2022:", total_rides_september)
print("Total rides in January 2022:", total_rides_january)

# Visualizing the data with a bar chart
months = ['January 2022', 'September 2022']
total_rides = [total_rides_january, total_rides_september]

plt.bar(months, total_rides, color=['blue', 'orange'])
plt.xlabel('Month')
plt.ylabel('Total Rides')
plt.title('Comparative Analysis of Bike Rides in January and September 2022')
plt.show()

# Calculate the total number of rides
total_rides = len(september_data)
print("Total rides in September 2022:", total_rides)

# Analyze the most common start locations
start_station_counts = september_data['start station name'].value_counts()
top_start_stations = start_station_counts.head(10)  # Top 10 start stations

# Visualizing the top start stations
top_start_stations.plot(kind='bar')
plt.xlabel('Start Station')
plt.ylabel('Number of Rides')
plt.title('Top 10 Start Stations for Blue Bikes in September 2022')
plt.show()

# Calculate the total number of rides
total_rides = len(january_data)
print("Total rides in September 2022:", total_rides)

# Analyze the most common start locations
start_station_counts = january_data['start station name'].value_counts()
top_start_stations = start_station_counts.head(10)  # Top 10 start stations

# Visualizing the top start stations
top_start_stations.plot(kind='bar')
plt.xlabel('Start Station')
plt.ylabel('Number of Rides')
plt.title('Top 10 Start Stations for Blue Bikes in January 2022')
plt.show()