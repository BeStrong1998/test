from bs4 import BeautifulSoup
from utils import get_html


def get_all_flats():# парсимим страницу на cian.ru по новострокам и берем от туда ссылку на конкретное обялвение
    html = get_html("https://www.cian.ru/kupit-kvartiru-novostroyki/")
    soup = BeautifulSoup(html, 'html.parser')
    flats_list = soup.find('div', class_="_93444fe79c--wrapper--W0WqH").find_all('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
    for flat in flats_list:
        url = flat.find('a')['href']
        print(url)