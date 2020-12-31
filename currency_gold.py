import requests
from bs4 import BeautifulSoup


def get_response(url):
    try:
        response = requests.get(url)
    except:
        return None

    if response.status_code == 200:
        return response

    return None


def mining_data(response, c_key):
    soup = BeautifulSoup(response.text, 'html.parser')
    sell_price = soup.find('td', attrs={'id': c_key[0]})
    buy_price = soup.find('td', attrs={'id': c_key[1]})

    currency_string = f'فروش: {sell_price.string.strip()}\n' \
                      f'خرید: {buy_price.string.strip()}\n'

    return currency_string


def currency_gold(key):
    link = 'https://www.bonbast.com/'
    res = get_response(link)
    return mining_data(res, key)



