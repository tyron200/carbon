import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
data_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv'
df = pd.read_csv(data_url)

# Step 2: Filter the data for Beef
beef_data = df[df['product'] == 'Beef']

# Step 3: Load world shapefile for mapping
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the world shapefile with the beef data on the 'country' column
merged_data = world.merge(beef_data, left_on='name', right_on='country')

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
merged_data.plot(column='co2_emission', cmap='OrRd',
                 linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Set plot title and labels
ax.set_title('Beef\'s Contribution to CO2 Emissions (kg/person/year)')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.tight_layout()

plt.show()

# This code will load the data, filter it to include only information related to Beef, and then map Beef's contribution to CO2 emissions using a world map visualization. The map will show the CO2 emissions (kg/person/year) for Beef in different countries, with color-coding to indicate the emission levels.
