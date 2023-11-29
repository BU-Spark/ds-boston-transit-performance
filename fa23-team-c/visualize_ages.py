import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("census_data.csv", skiprows=1)
df.set_index(df.columns[0], inplace=True)
df.to_csv("census.csv")

sorted_df = df.sort_values('Total:', ascending=False)
most_populated_regions = sorted_df.head(2).index.tolist()
least_populated_regions = sorted_df.tail(2).index.tolist()

age_columns = ['Total:.1', 'Total: aged 0-17']

def plot_age_composition(region_name):
    age_data = df.loc[region_name, age_columns]
    plt.figure(figsize=(8, 8))
    plt.pie(age_data, labels=['18+', '0 to 17'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Age Distribution of {region_name}')
    plt.show()

for region in most_populated_regions:
    plot_age_composition(region)

for region in least_populated_regions:
    plot_age_composition(region)
