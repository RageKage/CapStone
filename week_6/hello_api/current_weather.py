import requests
from pprint import pprint 
import os

def main():
    key = os.environ.get('WEATHER_KEY')
    location = get_location()
    print("Your location is: " + location)
    weather_data, error = get_current_weather(location, key)
    
    if error:
        print("Error getting weather data: " + str(error))
    else:
        print("Current weather")
        current_temp = get_temp(weather_data)
        for i in range(len(current_temp)):
            print(current_temp[i])



def get_location():
    city, country = '',''
    while len(city) == 0:
        city = input("Enter the city: ")
    while len(country) != 2 or not country.isalpha():
        country = input("Enter the country: ")
    
    return city + ',' + country


        

def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        url = "https://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except requests.exceptions.HTTPError as e:
        return None, e

def get_temp(data):
    try:
        country = data['sys']['country']
        city = data['name']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        
        return country, city, temp, description
    except Exception as e:
        return None, e
    
    
if __name__ == '__main__':
    main()
