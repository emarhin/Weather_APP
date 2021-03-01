from requests import get
import json

# THe IP address of the the user
ip = get('https://api.ipify.org').text


ipstack_key = "941ad35d4b1d5cb349abc036175d3ec2"
openweathermap_key = "6b3a463876d943d9474030e63265764f"

location_api = get(f"http://api.ipstack.com/{ip}?access_key={ipstack_key}")
location_json = json.loads(location_api.text)


# The longitude of your location
long = location_json["longitude"]

# The latitute of your location
lat = location_json["latitude"]


openweathermap_api = get(
    f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={openweathermap_key}")
openweathermap_json = json.loads(openweathermap_api.text)


print(openweathermap_json['main']['temp'])
print(openweathermap_json['main']['feels_like'])
print(openweathermap_json['main']['pressure'])
print(openweathermap_json['main']['humidity'])
