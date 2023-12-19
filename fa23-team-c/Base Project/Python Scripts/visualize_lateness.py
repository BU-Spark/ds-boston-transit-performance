import matplotlib.pyplot as plt
import pandas as pd

travel_times = pd.read_csv('travel_times.csv')
travel_times_2 = pd.read_csv('travel_times.csv')

travel_times['scheduled_travel_time'] = pd.to_datetime(travel_times['scheduled_travel_time'], format='mixed')
travel_times['travel_time'] = pd.to_datetime(travel_times['travel_time'], format='mixed')
travel_times_2['lateness'] = (travel_times['travel_time'] - travel_times['scheduled_travel_time']).dt.total_seconds() / 60
average_lateness_by_route = travel_times_2.groupby('route_id')['lateness'].mean()
sorted_routes = average_lateness_by_route.sort_values(ascending=True)
five_least_late = sorted_routes.head(10)
five_most_late = sorted_routes.tail(10).sort_values(ascending=False)
most_late_route_ids = five_most_late.index.get_level_values('route_id').tolist()
least_late_route_ids = five_least_late.index.get_level_values('route_id').tolist()

# print(most_late_route_ids)
# print(five_most_late)
# print(least_late_route_ids)
# print(five_least_late)

data = {}
data_2 = {}
for route_id in least_late_route_ids:
    route_data = travel_times_2[travel_times_2['route_id'] == route_id]
    route_delays = route_data['lateness'].tolist()
    data[route_id] = route_delays
    route_travel_times = route_data['travel_time'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1])).tolist()
    data_2[route_id] = route_travel_times

for route_id in most_late_route_ids:
    route_data = travel_times_2[travel_times_2['route_id'] == route_id]
    route_delays = route_data['lateness'].tolist()
    if route_id[-1] == "_":
        route_id = route_id[:-1]
    data[route_id] = route_delays
    route_travel_times = route_data['travel_time'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1])).tolist()
    data_2[route_id] = route_travel_times

most_late_route_ids[0] = most_late_route_ids[0][:-1]

df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()
df_2 = pd.DataFrame.from_dict(data_2, orient='index')
df_2 = df_2.transpose()

# ax = df[least_late_route_ids + most_late_route_ids].plot(kind='box', title='boxplot', showfliers=False)
# plt.xlabel("Route ID")
# plt.ylabel("Lateness (minutes)")
# plt.title('Lateness for Bus Routes', fontsize=20)
# plt.rcParams["figure.autolayout"] = True
# plt.show()

# ax2 = df_2[least_late_route_ids + most_late_route_ids].plot(kind='box', title='boxplot', showfliers=False)
# plt.xlabel("Route ID")
# plt.ylabel("Travel Time (minutes)")
# plt.title('Travel Times for Bus Routes Based on Lateness', fontsize=20)
# plt.rcParams["figure.autolayout"] = True
# plt.show()

least_late_delays = df[least_late_route_ids]
most_late_delays = df[most_late_route_ids]
least_late_travel_times = df_2[least_late_route_ids]
most_late_travel_times = df_2[most_late_route_ids]


plt.figure(figsize=(10, 6))
plt.bar(least_late_delays.columns, least_late_delays.mean(), color='skyblue')
plt.xlabel("Route ID")
plt.ylabel("Average Lateness (minutes)")
plt.title('Average Lateness for Least Late Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(most_late_delays.columns, most_late_delays.mean(), color='lightgreen')
plt.xlabel("Route ID")
plt.ylabel("Average Lateness (minutes)")
plt.title('Average Lateness for Most Late Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(least_late_travel_times.columns, least_late_travel_times.mean(), color='mediumseagreen')
plt.xlabel("Route ID")
plt.ylabel("Average Travel Time (minutes)")
plt.title('Average Travel Times for Least Late Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(most_late_travel_times.columns, most_late_travel_times.mean(), color='orange')
plt.xlabel("Route ID")
plt.ylabel("Average Travel Time (minutes)")
plt.title('Average Travel Times for Most Late Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()  
plt.show()
