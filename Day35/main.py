api_key = "1dcb8481a1afe10a993730da0629a9fb"

# 1. Get your latitude and longitude from latlong.net
latitude = "35.162441"
longtitude = "126.910339"

# 2. Make a request to the One Call API using the requests module
import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": latitude,
    "lon": longtitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# 3. Print out the HTTP status code that you get back
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status() # This takes some time to get the response
weather_data = response.json()

# 4. Print the response to the console
print(weather_data["weather"][0]["description"]) # We can get the weather description
print(weather_data["weather"][0]["id"]) # We can get the weather id
