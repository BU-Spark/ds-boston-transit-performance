import time
import requests
import os
import json

API_KEY = '02c52e9c052a43f6a3c013c26ef36fa3'
BASE_URL = 'https://api-v3.mbta.com/'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}
bus_ids_file_path = os.path.join("fa23-team-b", "MBTA", "Bus_Id.txt")
with open(bus_ids_file_path, 'r') as bus_ids_file:
    bus_ids = bus_ids_file.read().splitlines()

accessibility_directory = os.path.join("fa23-team-b", "data", "Accessibility")
if not os.path.exists(accessibility_directory):
    os.makedirs(accessibility_directory)

file_path = os.path.join(accessibility_directory, 'stops.json')

stop_id = {}

def call(bus_id):
    response = requests.get(f'{BASE_URL}stops?filter[route]={bus_id}', headers=headers)
    if response.status_code == 200:
        data = response.json()
        for stop in data['data']:
            stop_name = stop['attributes']['name']
            stop_longitude = stop['attributes']['longitude']
            stop_latitude = stop['attributes']['latitude']
            accessibility = stop['attributes']['wheelchair_boarding']
            
            wheelchair_increment = 0 if accessibility == 0 else 1 if accessibility == 1 else 0

            if stop_name not in stop_id:
                stop_id[stop_name] = {
                    'bus_ids': [bus_id],
                    'wheelchair': wheelchair_increment,
                    'longitude': stop_longitude,
                    'latitude': stop_latitude
                }
            else:
                if bus_id not in stop_id[stop_name]['bus_ids']:
                    stop_id[stop_name]['bus_ids'].append(bus_id)
                    stop_id[stop_name]['wheelchair'] += wheelchair_increment
    else:
        print(f"Failed with status code: {response.status_code}")

for bus_id in bus_ids:
    call(bus_id)
    print(bus_id)
    time.sleep(20)

with open(file_path, 'w') as file:
    json.dump(stop_id, file, indent=4)

print("Finished!")
