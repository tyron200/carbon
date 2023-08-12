import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
data_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv'
df = pd.read_csv(data_url)

# Step 2: Create a box plot to visualize the CO2 contributions of food levels
plt.figure(figsize=(10, 6))
food_levels = ['low', 'medium', 'high']

# Filter the data for each food level and plot the box plot
box_data = [df[df['food_level'] == level]['co2_emission']
            for level in food_levels]
plt.boxplot(box_data, labels=food_levels, showfliers=False)

plt.xlabel('Food Level')
plt.ylabel('CO2 Emission (kg/person/year)')
plt.title('CO2 Contributions of Food Levels')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# This code will load the data from the CSV file and create a box plot to visualize the CO2 contributions of different food levels (low, medium, and high). Each box in the plot represents the distribution of CO2 emissions for the corresponding food level.
