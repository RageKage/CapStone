import os 
import requests
from datetime import datetime

def main():
    key = os.environ.get('WEATHER_KEY')
    location = get_location()
    
    data, error = get_forecast(location, key)
    if error:
        print(f"An error occurred: {error}")
        return
    list_of_forecast = data['list']

    for i in list_of_forecast:
        date = i['dt_txt']
        temp = i['main']['temp']
        description = i['weather'][0]['description']
        wind_speed = i['wind']['speed']
        print(f'Date: {date}\nTemp: {temp} C\nDesc: {description}\nSpeed: {wind_speed}')
        print()

def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input("Enter the city: ")
    while len(country) != 2 or not country.isalpha():
        country = input("Enter the country: ")
    
    return city + ',' + country

def get_forecast(location, key):
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        url = "https://api.openweathermap.org/data/2.5/forecast"
        response = requests.get(url, params=query).json()
        return response, None
    except requests.exceptions.HTTPError as e:
        return None, e
    
if __name__ == '__main__':
    main()