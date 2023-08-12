import pandas as pd
import matplotlib.pyplot as plt
# Replace 'path_to_csv_file' with the actual file path or URL
data_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv'
df = pd.read_csv(data_url)

east_african_countries = ['Kenya', 'Uganda', 'Tanzania', 'Rwanda', 'Ethiopia']
df_east_africa = df[df['country'].isin(east_african_countries)]
average_co2_emission = df_east_africa.groupby(
    'category')['co2_emmission'].mean()
print(average_co2_emission)
#  plotting
plt.figure(figsize=(10, 6))
plt.bar(average_co2_emission.index, average_co2_emission.values)
plt.xlabel('Food Category')
plt.ylabel('Average CO2 Emission per Person')
plt.title(
    'Average CO2 Emission per Person by Food Category in East African Countries')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# This code will create a histogram with the food categories on the x-axis and the average CO2 emission per person on the y-axis. The plt.bar() function is used to create the histogram bars, and the plt.xlabel(), plt.ylabel(), and plt.title() functions are used to set the labels and title for the plot. The plt.xticks(rotation=45) is used to rotate the x-axis labels for better readability.
