import pandas as pd

stop_data = pd.read_csv('data/stops_zipcodes.csv')
neighborhood_data = pd.read_csv('data/neighborhoods_to_zipcodes.csv')

stop_data['zip_code'] = stop_data['zip_code'].astype(str).str.zfill(5)
neighborhood_data['ZipCodes'] = neighborhood_data['ZipCodes'].str.split(', ')

neighborhood_zip_codes = set()
for codes in neighborhood_data['ZipCodes']:
    for code in codes:
        neighborhood_zip_codes.add(code)

stop_zip_codes = set()
for code in stop_data["zip_code"]:
    stop_zip_codes.add(code)

missing_zip_codes = stop_zip_codes - neighborhood_zip_codes

if missing_zip_codes:
    with open('missing_zip_codes.txt', 'w') as file:
        file.write("Zip codes not in neighborhood data:\n")
        for code in missing_zip_codes:
            file.write(code + "\n")
    print("Missing zip codes have been saved to 'missing_zip_codes.txt'.")
else:
    print("All zip codes from stop data are present in neighborhood data.")