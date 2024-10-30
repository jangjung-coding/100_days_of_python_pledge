api_key = "1dcb8481a1afe10a993730da0629a9fb"

# 1. Get your latitude and longitude from latlong.net
latitude = "33.44"
longtitude = "-94.04"

# 2. Make a request to the One Call API using the requests module
import requests

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": latitude,
    "lon": longtitude,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code) # This takes some time to get the response
print(response.json())

# 3. Print out the HTTP status code that you get back

# 4. Print the response to the console

# 5. Copy-paste the response to an online JSON viewer(e.g. jsonviewer.stack.hu)

# 6. Locate the hourly forecast for the next 48 hours