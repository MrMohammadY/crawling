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


def mining_data(response):
    mobile_list = []
    soup = BeautifulSoup(response.content, 'html.parser')
    all_mobiles = soup.find_all(
        'div', attrs={'class': 'is-plp'}
    )
    for m in all_mobiles:
        mobile_list.append(f'مدل: {m["data-title-en"]}\n'
                           f'قیمت: {m["data-price"]}\n')

    return mobile_list


def mobile(link):
    mobiles = mining_data(get_response(link))
    return mobiles
