import csv
import requests
import Constants

def reverse_geocode(lat, lng):
    api_key = Constants.GOOGLE_MAPS_KEY
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    params = {
        'latlng': f"{lat},{lng}",
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    zip_code = None
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            for component in result['results'][0]['address_components']:
                if 'postal_code' in component['types']:
                    zip_code = component['long_name']
                    # print(f"Zip Code: {zip_code}")
                    break
            else:
                print("Zip code not found for this location.")
        else:
            print(f"Reverse geocoding failed. Status: {result['status']}")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    return zip_code


input_file = 'data/stops_coordinates.csv'
output_file = 'stops_zipcodes.csv'

with open(input_file, 'r') as csvfile, open(output_file, 'w', newline='') as outputcsv:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames + ['zip_code']
    
    writer = csv.DictWriter(outputcsv, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        stop_id = row['stop_id']
        lat = row['latitude']
        lon = row['longitude']        
        zip_code = reverse_geocode(lat, lon)
        writer.writerow({**row, 'zip_code': zip_code})
