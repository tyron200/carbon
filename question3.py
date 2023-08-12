import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Load the data from the CSV file
data_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv'
df = pd.read_csv(data_url)

# Step 2: Group the data by "category" to separate animal and non-animal products
grouped_data = df.groupby('category')

# Step 3: Calculate the total consumption and average carbon footprint for each category
consumption_impact = grouped_data.agg({
    'consumption': 'sum',
    'co2_emission': 'mean'
})

# Step 4: Display the findings in a tabular format
print(consumption_impact)

# Create a bar graph to visualize the consumption and carbon footprint impact
plt.figure(figsize=(10, 6))

# Plot consumption as blue bars
plt.bar(consumption_impact.index,
        consumption_impact['consumption'], color='skyblue', label='Consumption')

# Plot carbon footprint impact as red line
plt.plot(consumption_impact.index,
         consumption_impact['co2_emission'], color='red', marker='o', label='Carbon Footprint Impact')

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Consumption and Carbon Footprint Impact of Animal and Non-Animal Products')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()
