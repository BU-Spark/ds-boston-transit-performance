import pandas as pd
import requests
import pprint
from time import sleep

bus_stops = pd.read_csv('data/PATI_BUS_Stops.csv')
list_of_zip_codes = []
pp = pprint.PrettyPrinter(compact=True)
columns = list(bus_stops.columns)

# iterate over rows of bus_stops dataframe
for index, row in bus_stops.iterrows():
    # do something with each row
    print(row["Stop_ID"])

    # define the url and parameters
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"""{row["Latitude"]},{row["Longitude"]}""",
        "key": "AIzaSyD6NeK7pHH8jL2ogy_kB9B3qnGtVbpUHuM"
    }

    # send the request and get the response
    response = requests.get(url, params=params)

    # convert the response to a dictionary
    data = response.json()

    # print(data['results'][0]['address_components'][0]['long_name'])
    try:
        # raise Exception("Sorry, no numbers below zero") 
        for item in data['results'][0]['address_components']:
            if item['types'] == ['postal_code']:
                zip_code = item['long_name']
                row_list = list(row)
                row_list.append(zip_code)
                list_of_zip_codes.append(row_list)
                break
    except:
        print(f'No postal code found for {row["Stop_ID"]}')
        with open('data/failed_stop_ids.txt', 'a') as f:
            f.write(str(row["Stop_ID"]) + '\n')
            f.close()
        continue
    
    if index == 5:
        break
    sleep(0.05)
        # use the data dictionary
        # pp.pprint(data)

# print(list_of_zip_codes)
df = pd.DataFrame(list_of_zip_codes, columns=columns + ['zip_code'])
df.to_csv('data/bus_stops_with_zip_codes_google.csv', index=False)

