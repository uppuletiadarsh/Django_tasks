import requests
from django.shortcuts import render

def get_weather_data(city):
    API_KEY = 'a078e3c64d183a25b11a9ccb25d9712d'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric'  
    response = requests.get(url)
    return response.json()

def weather_view(request):
    weather_data = {}
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        if city_name:
            weather_data = get_weather_data(city_name)
            if weather_data.get('cod') != 200: 
                weather_data = {'error': 'Enter a proper city name'}
        else:
            weather_data = {'error': 'City name cannot be empty'}
    return render(request, 'weather.html', {'weather_data': weather_data})
