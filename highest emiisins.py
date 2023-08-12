import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
data_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv'
df = pd.read_csv(data_url)

# Step 2: Group the data by country and calculate the total emissions for each country
country_emissions = df.groupby('country')['co2_emission'].sum().reset_index()

# Step 3: Sort the countries based on emissions and select the top 10 countries
top_10_countries = country_emissions.nlargest(10, 'co2_emission')

# Step 4: Create a bar chart to visualize the emissions for the top 10 countries
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries['country'],
        top_10_countries['co2_emission'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('CO2 Emission (kg/person/year)')
plt.title('Top 10 Countries with Highest CO2 Emissions')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# This code will load the data from the CSV file, calculate the total emissions for each country, and then create a bar chart to visualize the emissions for the top 10 countries with the highest CO2 emissions. Each bar represents a country, and the height of the bar corresponds to its total emissions.
