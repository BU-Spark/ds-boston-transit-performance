import pandas as pd
import requests
import csv

# data = pd.read_csv('MBTA-Bus-Arrival-Departure-Times_2022-01.csv')
# unique_stops_routes = data.groupby('stop_id')['route_id'].unique().reset_index()

# unique_stops_routes.to_csv('stops.csv', index=False)

def get_stop_info(stop_id, api_key):
    url = f"https://api-v3.mbta.com/stops/{stop_id}"
    headers = {"X-API-Key": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        stop_data = response.json()
        return stop_data
    else:
        print(f"Error getting stop info for {stop_id}: {response.status_code}")
        return None

df = pd.read_csv('stops.csv')
stop_ids = df['stop_id'].tolist()
API_KEY = "fff28dec8ca849b294db17c6aebede8b"
stops_data = []

for stop_id in stop_ids:
    stop_info = get_stop_info(stop_id, API_KEY)
    if stop_info:
        latitude = stop_info['data']['attributes']['latitude']
        longitude = stop_info['data']['attributes']['longitude']
        stops_data.append([stop_id, latitude, longitude])

csv_file_path = 'stops_coordinates.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['stop_id', 'latitude', 'longitude'])
    writer.writerows(stops_data)