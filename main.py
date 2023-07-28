import requests
import json
import os

lat = input("Please enter Latitude: ")
lon = input("Please enter Longitude: ")

open_source_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true" 

raw_data = requests.get(open_source_url)
weather_data = json.loads(raw_data.text)
temp_in_celsius = weather_data['current_weather']['temperature'] 
os.system(f"say 'The current temperature is {temp_in_celsius} degrees celsius'")  