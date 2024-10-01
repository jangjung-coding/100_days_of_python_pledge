# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data[:5])

# import pandas as pd

# weather = pd.read_csv('weather_data.csv')
# print(weather.head())

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data['Primary Fur Color'].value_counts())