import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

URL = 'http://goatofski.ru'


def find_price(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("td", class_="ver12").get_text()
    converted_price = re.sub(r'\D', '', price)
    if int(converted_price) < 5000:
        return converted_price
    else:
        return 'Цена равняется ' + converted_price


print(find_price(URL))
