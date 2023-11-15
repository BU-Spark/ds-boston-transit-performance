import pandas as pd
import requests
import pprint
from time import sleep
import requests
import random

bus_stops = pd.read_csv('data/PATI_BUS_Stops.csv')
list_of_zip_codes = []
pp = pprint.PrettyPrinter(compact=True)
columns = list(bus_stops.columns)

# iterate over rows of bus_stops dataframe
for index, row in bus_stops.iterrows():
    # do something with each row
    print(row["Stop_ID"], row["Latitude"], row["Longitude"])

    # define the url and parameters

    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "format": "geocodejson",
        "lat": f'{row["Latitude"]}',
        "lon": f'{row["Longitude"]}'
    }

    response = requests.get(url, params=params)
    # print(response.content)

    # convert the response to a dictionary
    data = response.json()

    # print(data['results'][0]['address_components'][0]['long_name'])
    try:
        # raise Exception("Sorry, no numbers below zero")
        zip_code = data['features'][0]['properties']['geocoding']['postcode']
        row_list = list(row)
        row_list.append(zip_code)
        list_of_zip_codes.append(row_list)
    except:
        print(f'No postal code found for {row["Stop_ID"]}')
        with open('data/failed_stop_ids.txt', 'a') as f:
            f.write(str(row["Stop_ID"]) + '\n')
            f.close()
        continue

    # generate a random number between 1 and 10
    random_number = random.randint(1, 100)

    # sleep for the random number of seconds
    sleep(random_number*0.001)
    sleep(0.09)
        # use the data dictionary
        # pp.pprint(data)

# print(list_of_zip_codes)
df = pd.DataFrame(list_of_zip_codes, columns=columns + ['zip_code'])
df.to_csv('data/bus_stops_with_zip_codes_open.csv', index=False)

