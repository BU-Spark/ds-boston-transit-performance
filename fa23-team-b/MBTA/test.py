import requests
import os
import time

API_KEY = '02c52e9c052a43f6a3c013c26ef36fa3'
BASE_URL = 'https://api-v3.mbta.com/'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}
bus_ids_file_path = os.path.join("fa23-team-b", "MBTA", "Bus_Id.txt")
with open(bus_ids_file_path, 'r') as bus_ids_file:
    bus_ids = bus_ids_file.read().splitlines()
# bus_ids = ["741", "742", "743", "751", "749", "746", "747", "708"]

accessibility_directory = os.path.join("fa23-team-b", "data", "Accessibility")
if not os.path.exists(accessibility_directory):
    os.makedirs(accessibility_directory)

file_path = os.path.join(accessibility_directory, 'stops.txt')

stop_id = set()

def call(bus_id):
    # Make API request for bus stops on the specified route    
        response = requests.get(f'{BASE_URL}stops?filter[route]={bus_id}', headers=headers)
        if response.status_code == 200:
            data = response.json()

            for stop in data['data']:
                stop_name = stop['attributes']['name']
                stop_id.add(f"{stop_name}")
        else:
            print(f"Failed with status code: {response.status_code}")
                    
# for bus_id in bus_ids:
#      call(bus_id)
#      time.sleep(20)

call('741')
call('742')
call('743')
call('751')
call('749')
# call(746)
# call(747)
# call(708)
# call(1)
# call(4)
# call(7)
# call(8)
# call(9)
# call(10)
# call(11)
# call(14)
# call(15)
# call(16)
# call(17)
# call(18)
# call(19)
# call(21)
# call(22)
# call(23)
# call(24)
# call(26)
# call(28)
# call(29)
# call(30)
# call(31)
# call(32)
# call(33)
# call(34)
# call(34E)
# call(35)
# call(36)
# call(37)
# call(38)
# call(39)
# call(40)
# call(41)
# call(42)
# call(43)
# call(44)
# call(45)
# call(47)
# call(50)
# call(51)
# call(52)
# call(55)
# call(57)
# call(59)
# call(60)
# call(61)
# call(62)
# call(627)
# call(64)
# call(65)
# call(66)
# call(67)
# call(68)
# call(69)
# call(70)
# call(71)
# call(73)
# call(74)
# call(75)
# 76
# 77
# 78
# 80
# 83
# 85
# 86
# 87
# 88
# 89
# 90
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 99
# 100
# 101
# 104
# 105
# 106
# 108
# 109
# 110
# 111
# 112
# 114
# 116
# 117
# 119
# 120
# 121
# 131
# 132
# 134
# 137
# 171
# 201
# 202
# 210
# 211
# 215
# 216
# 217
# 220
# 222
# 225
# 226
# 230
# 236
# 238
# 240
# 245
# 350
# 351
# 354
# 411
# 424
# 426
# 428
# 429
# 430
# 435
# 436
# 439
# 441
# 442
# 450
# 451
# 455
# 456
# 501
# 504
# 505
# 553
# 554
# 556
# 558
# 712
# 713
# 714
# 716



with open(file_path, 'w') as file:
        for stop in stop_id:
            file.write(f"{stop}\n")
print("finished!\n")