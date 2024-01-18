import requests
import os
API_KEY = '02c52e9c052a43f6a3c013c26ef36fa3'
BASE_URL = 'https://api-v3.mbta.com/'


headers = {
    'Authorization': f'Bearer {API_KEY}'
}

params = {
    "filter[type]": "3"  # Filtering for buses
}
response = requests.get(f'{BASE_URL}routes', headers=headers, params=params)


route_ids = []
accessibility_directory = os.path.join("fa23-team-b/data", "Accessibility")
if not os.path.exists(accessibility_directory):
    os.makedirs(accessibility_directory)

file_path = os.path.join(accessibility_directory, 'Bus_Id.txt')


with open(file_path, 'w') as file:


    if response.status_code == 200:
        data = response.json()
        
        for route in data['data']:
            route_id = route['id']
            route_ids.append(route_id)
            file.write(f"{route_id}\n")
    else:
        print(f"Failed with status code: {response.status_code}")