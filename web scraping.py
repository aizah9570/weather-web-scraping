import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://weather.com/weather/today/l/PKXX0004:1:PK'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    location = soup.find('h1', class_='CurrentConditions--location--1Ayv3').text
    temperature = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ').text
    condition = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text

    data = {
        'Location': [location],
        'Temperature': [temperature],
        'Condition': [condition]
    }
    df = pd.DataFrame(data)
    df.to_csv('islamabad_weather_data.csv', index=False)

    print("Weather data has been successfully scraped and saved to islamabad_weather_data.csv")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
