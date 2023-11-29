import matplotlib.pyplot as plt
import pandas as pd

delays = pd.read_csv('data/delays.csv')
travel_times = pd.read_csv('data/travel_times.csv')

delays['abs_delay'] = delays['delay'].abs()
average_delay_by_route = delays.groupby('route_id')['abs_delay'].mean()
sorted_routes = average_delay_by_route.sort_values(ascending=True)
five_most_punctual = sorted_routes.head(5)
five_least_punctual = sorted_routes.tail(5).sort_values(ascending=False)
most_punctual_route_ids = five_most_punctual.index.get_level_values('route_id').tolist()
least_punctual_route_ids = five_least_punctual.index.get_level_values('route_id').tolist()

# print(most_punctual_route_ids)
# print(five_most_punctual)
# print(least_punctual_route_ids)
# print(five_least_punctual)

data = {}
data_2 = {}
for route_id in most_punctual_route_ids:
    route_data = delays[delays['route_id'] == route_id]
    route_data_2 = travel_times[travel_times['route_id'] == route_id]
    route_delays = route_data['delay'].tolist()
    route_travel_times = route_data_2['travel_time'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1])).tolist()
    data[route_id] = route_delays
    data_2[route_id] = route_travel_times

for route_id in least_punctual_route_ids:
    route_data = delays[delays['route_id'] == route_id]
    route_data_2 = travel_times[travel_times['route_id'] == route_id]
    route_delays = route_data['delay'].tolist()
    route_travel_times = route_data_2['travel_time'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1])).tolist()
    if route_id[-1] == "_":
        route_id = route_id[:-1]
    data[route_id] = route_delays
    data_2[route_id] = route_travel_times

least_punctual_route_ids[2] = least_punctual_route_ids[2][:-1]

df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()
df_2 = pd.DataFrame.from_dict(data_2, orient='index')
df_2 = df_2.transpose()

# ax = df[most_punctual_route_ids + least_punctual_route_ids].plot(kind='box', title='boxplot', showfliers=False)
# plt.xlabel("Route ID")
# plt.ylabel("Delay (minutes)")
# plt.title('Punctuality for Bus Routes', fontsize=20)
# plt.rcParams["figure.autolayout"] = True
# plt.show()

# ax2 = df_2[most_punctual_route_ids + least_punctual_route_ids].plot(kind='box', title='boxplot', showfliers=False)
# plt.xlabel("Route ID")
# plt.ylabel("Travel Time (minutes)")
# plt.title('Travel Times for Bus Routes Based on Punctuality', fontsize=20)
# plt.rcParams["figure.autolayout"] = True
# plt.show()

least_punctual_delays = df[least_punctual_route_ids]
most_punctual_delays = df[most_punctual_route_ids]
least_punctual_travel_times = df_2[least_punctual_route_ids]
most_punctual_travel_times = df_2[most_punctual_route_ids]

plt.figure(figsize=(10, 6))
plt.bar(least_punctual_delays.columns, least_punctual_delays.mean().abs(), color='lightgreen')
plt.xlabel("Route ID")
plt.ylabel("Average Absolute Delay (minutes)")
plt.title('Average Absolute Delay for Least Punctual Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(most_punctual_delays.columns, most_punctual_delays.mean().abs(), color='skyblue')
plt.xlabel("Route ID")
plt.ylabel("Average Absolute Delay (minutes)")
plt.title('Average Absolute Delay for Most Punctual Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(least_punctual_travel_times.columns, least_punctual_travel_times.mean(), color='orange')
plt.xlabel("Route ID")
plt.ylabel("Average Travel Time (minutes)")
plt.title('Average Travel Times for Least Punctual Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(most_punctual_travel_times.columns, most_punctual_travel_times.mean(), color='mediumseagreen')
plt.xlabel("Route ID")
plt.ylabel("Average Travel Time (minutes)")
plt.title('Average Travel Times for Most Punctual Bus Routes', fontsize=16)
plt.xticks()
plt.tight_layout()  
plt.show()
