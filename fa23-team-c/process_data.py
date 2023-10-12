import pandas as pd

def filter_data(df):
    filtered_df = df[df['point_type'].isin(['Startpoint', 'Endpoint'])]
    return filtered_df

def calculate_travel_times(df):
    grouped = df.groupby(['direction_id', 'half_trip_id'])
    travel_times = []

    for (direction, trip_id), group in grouped:
        startpoint = group[group['point_type'] == 'Startpoint']
        endpoint = group[group['point_type'] == 'Endpoint']

        startpoint_actual = startpoint['actual'].values[0]
        endpoint_actual = endpoint['actual'].values[0]
        service_date = group['service_date'].values[0]

        startpoint_actual = pd.to_datetime(startpoint_actual, format='%Y-%m-%d %H:%M:%S.%f')
        endpoint_actual = pd.to_datetime(endpoint_actual, format='%Y-%m-%d %H:%M:%S.%f')

        travel_time = endpoint_actual - startpoint_actual
        if travel_time.days == 0:
            hours, remainder = divmod(travel_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_travel_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        route_id = group['route_id'].values[0]

        travel_times.append({
            'half_trip_id': trip_id,
            'service_date': service_date,
            'route_id': route_id,
            'direction_id': direction,
            'travel_time': formatted_travel_time})

    travel_times_df = pd.DataFrame(travel_times)
    return travel_times_df

# df = pd.read_csv("MBTA-Bus-Arrival-Departure-Times_2022-01.csv")
# filtered_df = filter_data(df)
# filtered_df.to_csv("filtered_data.csv", index=False)
# travel_times_df = calculate_travel_times(filtered_df)
# travel_times_df.to_csv("travel_times.csv", index=False)

travel_times_df = pd.read_csv("travel_times.csv")

average_travel_times = travel_times_df.groupby(['route_id', 'direction_id'])['travel_time'].apply(
    lambda x: round(pd.to_timedelta(x).mean().total_seconds() / 60, 1)
)
average_travel_times = average_travel_times.reset_index()
average_travel_times = average_travel_times.rename(columns={'travel_time': 'average_travel_time'})

# average_travel_times.to_csv("average_travel_times.csv", index=False)