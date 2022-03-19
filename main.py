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

    bitlink_response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    bitlink_response.raise_for_status()
    return bitlink_response.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': token}
    params = {'unit': 'day', 'units': '-1'}

    if ('http' or 'https') in url:
        url = url_without_scheme(url)

    bitlink_response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
                                 headers=headers, params=params)
    bitlink_response.raise_for_status()
    return bitlink_response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': token}

    if ('http' or 'https') in url:
        url = url_without_scheme(url)

    bitlink_response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    if bitlink_response.ok:
        return True
    return False


def main():
    load_dotenv()
    access_token = os.getenv('BITLY_ACCESS_TOKEN')

    user_url = input('Введите ссылку: ')
    try:
        if is_bitlink(access_token, user_url):
            print(count_clicks(access_token, user_url))
        else:
            print(shorten_link(access_token, user_url))
    except NameError as name_error:
        print(name_error)
    except HTTPError as error:
        print(error)


if __name__ == '__main__':
    main()
