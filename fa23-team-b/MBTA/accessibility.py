import requests
import os

API_KEY = '02c52e9c052a43f6a3c013c26ef36fa3'
BASE_URL = 'https://api-v3.mbta.com/'


headers = {
    'Authorization': f'Bearer {API_KEY}'
}
route_id = "57"

response = requests.get(f'{BASE_URL}stops?filter[route]={route_id}', headers=headers)

accessibility_directory = os.path.join("fa23-team-b/data", "Accessibility")
if not os.path.exists(accessibility_directory):
    os.makedirs(accessibility_directory)

file_path = os.path.join(accessibility_directory, 'BUS_57_stops_accessibility.txt')


with open(file_path, 'w') as file:

    if response.status_code == 200:
        data = response.json()

        for stop in data['data']:
            stop_name = stop['attributes']['name']
            accessibility = stop['attributes']['wheelchair_boarding']

            if accessibility == 1:
                file.write(f"{stop_name}: Accessible\n")
            elif accessibility == 2:
                file.write(f"{stop_name}: Not Accessible\n")
            else:
                file.write(f"{stop_name}: No information available\n")
    else:
        file.write(f"Failed with status code: {response.status_code}")
