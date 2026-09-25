import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "fcb4a3ee18345159d142a5d75b04eeb1"

weather_params = {
    "lat": 33.046893,
    "lon": 73.570783,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])