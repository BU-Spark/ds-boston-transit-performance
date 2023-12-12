import pandas as pd

def calculate_lateness_for_dataframe_updated(df):
    # Convert scheduled and actual time columns to datetime format using the correct format
    df['scheduled_datetime'] = pd.to_datetime(df['scheduled'], format='%Y-%m-%d %H:%M:%S.%f')
    df['actual_datetime'] = pd.to_datetime(df['actual'], format='%Y-%m-%d %H:%M:%S.%f')
    
    # Calculate lateness by subtracting scheduled time from actual time
    df['lateness'] = (df['actual_datetime'] - df['scheduled_datetime']).dt.total_seconds() / 60  # in minutes
    
    return df


def generate_service_disparity_data(df):
    # Group by route_id and calculate average lateness for all trips, count of all trips,
    # and average lateness for late occurrences only
    grouped = df.groupby('route_id').agg({
        'lateness': ['mean', 'count', lambda x: x[x > 0].mean()],
        'half_trip_id': lambda x: (x[df['lateness'] > 0].count() / x.count()) * 100  # % of late occurrences
    }).reset_index()
    
    # Rename columns
    grouped.columns = ['route_id', 'average_lateness_all', 'total_trips', 'average_lateness_late_only', 'percent_late']
    
    # Sort by percentage of late occurrences
    grouped = grouped.sort_values(by='percent_late', ascending=False)
    
    return grouped

# Load your data
df = pd.read_csv("MBTA-Bus-Arrival-Departure-Times_2022-01.csv")

# Calculate lateness using the updated function
df_with_lateness_updated = calculate_lateness_for_dataframe_updated(df)

# Generate disparity data
service_disparities_df_updated = generate_service_disparity_data(df_with_lateness_updated)

# Save the result to a CSV file
service_disparities_df_updated.to_csv("service_disparities_updated.csv", index=False)
