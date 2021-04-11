import requests
def api_for_weather(place):
    result = requests.get(
        'http://openweathermap.org/data/2.5/weather?q=' + place + '&appid=486d45a8672282f2149439e3fc7bfe40')
    data = result.json()
    return data

print(api_for_weather('ANANTAPUR'))