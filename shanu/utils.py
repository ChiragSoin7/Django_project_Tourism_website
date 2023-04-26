import requests

def get_weather_data(city_name):
    # Replace the API key with your own API key
    api_key = 'your_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()