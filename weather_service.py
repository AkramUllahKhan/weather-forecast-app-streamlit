import requests
import datetime

def get_weather_data(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_data(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def process_forecast_data(forecast_data):
    list_of_forecasts = forecast_data['list']
    forecast_by_day = {}
    for entry in list_of_forecasts:
        timestamp = entry['dt_txt']
        date = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').date()
        if date not in forecast_by_day:
            forecast_by_day[date] = []
        forecast_by_day[date].append(entry['main'])
    return forecast_by_day
