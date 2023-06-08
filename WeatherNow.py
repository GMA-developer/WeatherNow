import requests
import json


def city_id():
    city = input('Введите название города: ')
    city = city.title()
    return city

city = city_id()

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
# weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = weather_data['wind']['speed']

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
