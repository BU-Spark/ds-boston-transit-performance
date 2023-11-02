import pandas as pd

df = pd.read_csv('filtered_data.csv')

grouped = df.groupby(['direction_id', 'half_trip_id'])
travel_times = []

for (direction, trip_id), group in grouped:
    startpoint = group[group['point_type'] == 'Startpoint']
    endpoint = group[group['point_type'] == 'Endpoint']

    startpoint_actual = startpoint['actual'].values[0]
    startpoint_scheduled = startpoint['scheduled'].values[0]
    endpoint_actual = endpoint['actual'].values[0]
    endpoint_scheduled = endpoint['scheduled'].values[0]
    service_date = group['service_date'].values[0]

    startpoint_actual = pd.to_datetime(startpoint_actual, format='%Y-%m-%d %H:%M:%S.%f')
    startpoint_scheduled = pd.to_datetime(startpoint_scheduled, format='%Y-%m-%d %H:%M:%S.%f')
    endpoint_actual = pd.to_datetime(endpoint_actual, format='%Y-%m-%d %H:%M:%S.%f')
    endpoint_scheduled = pd.to_datetime(endpoint_scheduled, format='%Y-%m-%d %H:%M:%S.%f')

    travel_time = endpoint_actual - startpoint_actual
    scheduled_travel_time = endpoint_scheduled - startpoint_scheduled

    if travel_time.days == 0:
        hours, remainder = divmod(travel_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_travel_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    hours, remainder = divmod(scheduled_travel_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_scheduled_travel_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    route_id = group['route_id'].values[0]

    travel_times.append({
        'half_trip_id': trip_id,
        'service_date': service_date,
        'route_id': route_id,
        'direction_id': direction,
        'scheduled_travel_time': formatted_scheduled_travel_time,
        'travel_time': formatted_travel_time})

travel_times_df = pd.DataFrame(travel_times)

travel_times_df.to_csv('travel_times.csv')