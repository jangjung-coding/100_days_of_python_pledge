# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data[:5])

import pandas as pd

weather = pd.read_csv('weather_data.csv')
print(weather.head())