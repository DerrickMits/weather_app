import requests # type: ignore
from django.shortcuts import render # type: ignore

def get_weather(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data = {'error': 'City not found'}
    return render(request, 'weather/weather.html', {'weather_data': weather_data})
