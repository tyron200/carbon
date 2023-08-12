import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
data_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv'
df = pd.read_csv(data_url)

# Step 2: Calculate the difference between consumption and emissions
df['difference'] = df['co2_emission'] - df['consumption']

# Step 3: Find the food product with the largest difference
max_difference_food = df.loc[df['difference'].idxmax(), 'product']
max_difference = df['difference'].max()

# Step 4: Create a bar plot to visualize the differences
plt.figure(figsize=(10, 6))
plt.bar(df['product'], df['difference'], color='skyblue')
plt.xlabel('Food Product')
plt.ylabel('Difference between Consumption and Emissions')
plt.title('Difference between Consumption and Emissions for Food Products')
# Adding a horizontal line at y=0 for reference
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.xticks(rotation=45)
plt.tight_layout()

# Step 5: Highlight the food product with the largest difference
plt.annotate(f'Max Difference: {max_difference}', xy=(df.index[df['difference'].idxmax()], max_difference),
             xytext=(df.index[df['difference'].idxmax()] +
                     0.2, max_difference + 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()

# This code will create a bar graph with blue bars representing the consumption of animal and non-animal products and a red line with markers showing the carbon footprint impact. The x-axis will have the categories (animal and non-animal products), and the y-axis will have the corresponding values.