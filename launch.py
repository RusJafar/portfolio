import argparse
import parsersite
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Введите адрес сайта")
args = parser.parse_args()

#######################################################################################################################
URL = input("Ведите адрес сайта:\n")

def is_url(url):
    '''Проверяем введенный URL'''
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

 #######################################################################################################################   


if is_url(URL):
    print(URL)
    print('Начинаю парсить сайт!')
    p = parsersite.Parser(URL)
    p.pars()
else:
    print('URL-адрес указан неверно!')