import requests
from bs4 import BeautifulSoup
# import time
import pyowm

dollar_hr = 'https://minfin.com.ua/ua/currency/banks/kharkov/usd/'
euro_hr = 'https://minfin.com.ua/ua/currency/banks/kharkov/eur/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


def check_carrency():
    full_page = requests.get(dollar_hr, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span",{"class":"DFlfde", "class": "SwHCTb", "data-precision": "2"})
    print('Сейчас курс доллара = ' + convert[0].text + ' грн.')
    # time.sleep(60)
    # check_carrency()


def get_weather():
    owm = pyowm.OWM('71a225bf9495530081f8c057c514003e')

    obs = owm.weather_at_place('Kharkiv')
    w = obs.get_weather()
    temperature = w.get_temperature(unit = 'celsius')
    status = w.get_status()
    print('Weather in Kharkov: ' + str(temperature['temp']) + '°C ' + status)


get_weather()
check_carrency()
