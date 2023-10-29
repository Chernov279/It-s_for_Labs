import requests

api_key = "9a9d085c7f2d8e6463367a04d73047bf"

city = input('City name: ').strip().capitalize()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
# s = "https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&APPID=9a9d085c7f2d8e6463367a04d73047bf"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    desc = data['weather'][0]['description']
    temperature_for_me = data['main']['feels_like']
    visibility = data['visibility']
    print(f'Temperature: {temperature} C')
    print(f'Temperature feels like : {temperature_for_me} C')
    print(f'Weather description: {desc}')
    print(f'Visibility: {visibility / 100}%')
else:
    print('Ошибка в названии города или ответе сервера')
