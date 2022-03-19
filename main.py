import os
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests
from requests import HTTPError


def url_with_scheme(url):
    parse_url = urlparse(url)
    return f'https://{parse_url.geturl()}'


def url_without_scheme(url):
    parse_url = urlparse(url)
    return parse_url._replace(scheme="").geturl().replace('//', '', 1)


def shorten_link(token, url):
    headers = {'Authorization': token}
    payload = {'long_url': url}

    if ('http' or 'https') not in url:
        url = url_with_scheme(url)
        payload = {'long_url': url}

    bitlink = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    bitlink.raise_for_status()
    return bitlink.json()


def count_clicks(token, url):
    headers = {'Authorization': token}
    params = {'unit': 'day', 'units': '-1'}

    if ('http' or 'https') in url:
        url = url_without_scheme(url)

    number_clicks = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
                                 headers=headers, params=params)
    number_clicks.raise_for_status()
    return number_clicks.json()


def is_bitlink(token, url):
    headers = {'Authorization': token}

    if ('http' or 'https') in url:
        url = url_without_scheme(url)

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    if response.ok:
        return True
    return False


def main():
    load_dotenv()
    access_token = os.getenv('ACCESS_TOKEN')

    user_url = input('Введите ссылку: ')
    try:
        if is_bitlink(access_token, user_url):
            print(count_clicks(access_token, user_url)['total_clicks'])
        else:
            print(shorten_link(access_token, user_url)['link'])
    except NameError as name_error:
        print(name_error)
    except HTTPError as error:
        print(error)


if __name__ == '__main__':
    main()
