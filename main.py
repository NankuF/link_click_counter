import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests
from requests import HTTPError

load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')


def shorten_link(token, url):
    headers = {'Authorization': token}
    payload = {'long_url': url}

    parse = urlparse(url)
    if not parse.scheme:
        normal_url = f'https://{parse.netloc}{parse.path}'
        payload = {'long_url': normal_url}

    bitlink = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    bitlink.raise_for_status()
    return bitlink.json()


def count_clicks(token, url):
    headers = {'Authorization': token}
    params = {'unit': 'day', 'units': '-1'}

    number_clicks = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
                                 headers=headers, params=params)
    number_clicks.raise_for_status()
    return number_clicks.json()


def is_bitlink(token, url):
    headers = {'Authorization': token}

    parse = urlparse(url)
    if parse.scheme:
        url = f'{parse.netloc}{parse.path}'

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    if response.ok:
        return count_clicks(token, url=response.json()['id'])['total_clicks']
    return shorten_link(token, url)['link']


if __name__ == '__main__':
    user_url = input('Введите ссылку: ')
    try:
        print(is_bitlink(access_token, user_url))
    except NameError as name_error:
        print(name_error)
    except HTTPError as error:
        print(error)
