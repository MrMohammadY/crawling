import requests
from bs4 import BeautifulSoup
from config import CAR_BRANDS


def get_response(url):
    try:
        response = requests.get(url)
    except:
        return None

    if response.status_code == 200:
        return response

    return None


def mining_data(response):
    cars_list = list()
    soup = BeautifulSoup(response.content, 'html.parser')
    model = soup.find_all('span', attrs={'class': 'sefr-model'})
    trim = soup.find_all('small', attrs={'class': 'sefr-trim'})
    price = soup.find_all('small', attrs={'class': 'sefr-price'})

    for i in range(len(model)):
        cars_list.append(
            f'نام: {model[i].string.strip()}\n'
            f'مدل: {trim[i].string}\n'
            f'قیمت: {price[i].string}\n'
        )

    return cars_list


def car(number_of_dict):
    link = 'https://bama.ir/price?brand={}'.format(CAR_BRANDS[number_of_dict])
    cars = mining_data(get_response(link))
    return cars
