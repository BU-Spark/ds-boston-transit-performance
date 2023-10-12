import requests

API_KEY = '02c52e9c052a43f6a3c013c26ef36fa3'
BASE_URL = 'https://api-v3.mbta.com/'


headers = {
    'Authorization': f'Bearer {API_KEY}'
}


response = requests.get(f'{BASE_URL}routes', headers=headers)


route_ids = []


if response.status_code == 200:
    data = response.json()
    
    for route in data['data']:
        route_id = route['id']
        route_ids.append(route_id)
        print(route_id)
else:
    print(f"Failed with status code: {response.status_code}")
