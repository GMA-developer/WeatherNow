import requests
import json
import os



from dotenv import load_dotenv
load_dotenv()



def city_id():
    city = input('Введите название города: ')
    city = city.title()
    return get_jsonfile(city)



def get_jsonfile(city):
    url = os.getenv('URL_WEATHER_FIRST') + city + os.getenv('URL_WEATHER_SECOND')
    weather_data = requests.get(url).json()
    # weather_data_structure = json.dumps(weather_data, indent=2)
    return get_data(weather_data, city)



def get_data(weather_data, city):
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    wind_speed = weather_data['wind']['speed']
    return print_info(temperature, temperature_feels, wind_speed, city)



def print_info(temperature, temperature_feels, wind_speed, city):
    if abs(temperature) >= 5 and abs(temperature) <= 20 or abs(temperature) % 10 == 0:
        print('Сейчас в городе', city, str(temperature), 'градусов')
    elif abs(temperature) % 10 in range(2,5):
        print('Сейчас в городе', city, str(temperature), 'градуса')
    elif abs(temperature) % 10 == 1:
        print('Сейчас в городе', city, str(temperature), 'градус')

    if abs(temperature_feels) >= 5 and abs(temperature_feels) <= 20 or abs(temperature_feels) % 10 == 0:
        print('Ощущается как', str(temperature_feels), 'градусов')
    elif abs(temperature_feels) % 10 in range(2,5):
        print('Ощущается как', str(temperature_feels), 'градуса')
    elif abs(temperature_feels) % 10 == 1:
        print('Ощущается как', str(temperature_feels), 'градус')

    print('Скорость ветра', str(wind_speed) ,"м/с")

    
    
if __name__ == '__main__':
    city_id()
