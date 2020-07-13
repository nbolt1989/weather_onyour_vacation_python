
import os

# OpenWeatherMap API Key
weather_api_key = os.environ.get('weather_api_key')

# Google API Key
g_key = os.environ.get('g_key')

print("weather: " + weather_api_key)
print('gkey: ' + g_key)

