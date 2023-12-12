import pandas as pd

data = pd.read_csv('MBTA-Bus-Arrival-Departure-Times_2022-01.csv')

delays = []
scheduled_start_time = None
headway_start_time = None

for index, row in data.iterrows():
    if row['point_type'] == 'Startpoint':
        if row['standard_type'] == 'Schedule':
            delay = pd.to_datetime(row['actual']) - pd.to_datetime(row['scheduled'])
            delays.append(delay.total_seconds() / 60) 
        else:
            delay = (row['headway']) - (row['scheduled_headway'])
            delays.append(delay / 60)
    else:
        delays.append(None)

data['delay'] = delays
new_df = data[['half_trip_id', 'service_date', 'route_id', 'direction_id', 'delay']].dropna()
new_df.to_csv("delays.csv", index=False)
