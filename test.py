import requests
from bs4 import BeautifulSoup
import re


covid_w = 'https://index.minfin.com.ua/ua/reference/coronavirus/'
covid_ua = 'https://index.minfin.com.ua/ua/reference/coronavirus/ukraine/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
covid = 'https://www.google.com/search?ei=SVqKXv6LFtH9rgTC3I34DQ&q=statistic+covid-19&oq=statistic+covid-19&gs_lcp=CgZwc3ktYWIQAzIGCAAQBxAeMgYIABAKEB46CAgAEAcQChAeOgUIABDNAjoGCAAQDRAeOgoIABANEAUQChAeSg0IFxIJMTAtMTEwZzk5SgoIGBIGMTAtNGc0UJmwAViXxQFgq8YBaABwAHgAgAFviAHiB5IBAzIuOJgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwi-1KfBqdLoAhXRvosKHUJuA98Q4dUDCAw&uact=5'



def get_statistic_ua():
	full_page_4 = requests.get(covid_ua, headers=headers)
	soup_corona_ua = BeautifulSoup(full_page_4.content, 'html.parser')
	selector_t = soup_corona_ua.find("strong", {"class": "black"})
	prepered_t = re.sub(r"\s+", u".", selector_t.text)

	selector_d = soup_corona_ua.find("strong", {"class": "red"})
	prepered_d = re.sub(r"\s+", u".", selector_d.text)

	selector_r = soup_corona_ua.find("strong", {"class": "green"})
	prepered_r = re.sub(r"\s+", u".", selector_r.text)

	print('total infected: ' + prepered_t + '\ndeath: ' + prepered_d + '\nrecovered: ' + prepered_r)

def get_statistic_w():
    full_page_3 = requests.get(covid, headers=headers)
    soup_corona_w = BeautifulSoup(full_page_3.content, 'html.parser')

    selector_t = soup_corona_w.findALL("tr", {"class": "vfaQvf"})
    print(selector_t)



get_statistic_w()
get_statistic_ua()
