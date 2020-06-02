# - *- coding: utf- 8 - *-
import telebot
import config
import requests
from bs4 import BeautifulSoup
# import time
import pyowm
from telebot import apihelper


apihelper.proxy = {'http':'http://10.10.1.10:3128'}
bot = telebot.TeleBot(config.TOKEN)
dollar_hr = 'https://www.google.com/search?ei=L4-LXuH5AcSsrgSzlZqgAw&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+&gs_lcp=CgZwc3ktYWIQAxgAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQRzoFCAAQxAI6BggAEBYQHkoNCBcSCTEwLTU2ZzEwNUoKCBgSBjEwLTRnMlDSXFidb2D4fmgDcAJ4AIABYIgB8gKSAQE0mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab'
euro_hr = 'https://www.google.com/search?ei=QI-LXufkGcOEwPAPgYi-EA&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_lcp=CgZwc3ktYWIQARgAMgUIABDEAjIGCAAQBxAeMgYIABAHEB4yAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOggIABAIEAcQHjoICAAQBxAeEBNKEAgXEgwxMC0xMDVnMTAxZzdKDAgYEggxMC0zZzdnM1Dh5TdYiIw4YLaVOGgDcAN4AIABZIgBqAeSAQM5LjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab'
covid_w = 'https://www.google.com/search?q=covid-19+statistic+ukraine'
covid_ua = 'https://www.google.com/search?q=covid-19+statistic+ukraine'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Ну здарова!')


@bot.message_handler(commands=['weather'])
def get_weather_kh(message):
    owm = pyowm.OWM('71a225bf9495530081f8c057c514003e')

    obs = owm.weather_at_place('Kharkiv')
    w = obs.get_weather()
    temperature = w.get_temperature(unit = 'celsius')
    status = w.get_detailed_status()
    # icon = w.get_weather_icon_name()
    weather_message = 'Weather in Kharkov: ' + str(temperature['temp']) + '°C\n' + status
    bot.send_message(message.chat.id, weather_message)


@bot.message_handler(commands=['rate'])
def get_course(message):
    full_page_1 = requests.get(dollar_hr, headers=headers, proxies=apihelper.proxy)
    soup_dollar = BeautifulSoup(full_page_1.content, 'html.parser')
    convert_1 = soup_dollar.select("div.dDoNo.vk_bk.gsrt span")

    full_page_2 = requests.get(euro_hr, headers=headers)
    soup_euro = BeautifulSoup(full_page_2.content, 'html.parser')
    convert_2 = soup_euro.select("div.dDoNo.vk_bk.gsrt span")

    rate_message = 'Dollar exchange rate = ' + str(convert_1[0].text) + '\nEuro exchange rate = ' + str(convert_2[0].text)

    bot.send_message(message.chat.id, rate_message)
    # time.sleep(60)
    # check_carrency()


@bot.message_handler(commands=['covid_world'])
def get_statistic_w(message):
    full_page_3 = requests.get(covid_w, headers=headers)
    soup_corona_w = BeautifulSoup(full_page_3.content, 'html.parser')
    print(soup_corona_w)

    selector_w = soup_corona_w.select("tr:contains('Worldwide') td div")
    print(selector_w)

    covid_w_message = 'World COVID-19 statistic' + '\nTotal infected: ' + selector_w[0].text + '\nRecovered: ' + selector_w[1].text + '\nDied: ' + selector_w[2].text
    bot.send_message(message.chat.id, covid_w_message)


@bot.message_handler(commands=['covid_ukr'])
def get_statistic_ua(message):
    full_page_4 = requests.get(covid_ua, headers=headers)
    soup_corona_ua = BeautifulSoup(full_page_4.content, 'html.parser')

    selector_ua = soup_corona_ua.select("tr:contains('Ukraine') td div")
    print(selector_ua)

    covid_ua_message = 'Ukrainian COVID-19 statistic' + '\nTotal infected: ' + selector_ua[0].text + '\nRecovered: ' + selector_ua[1].text + '\nDied: ' + selector_ua[2].text
    bot.send_message(message.chat.id, covid_ua_message)

bot.polling(none_stop=True)