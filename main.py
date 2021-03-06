import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def get_url_without_scheme(url):
    parsed_url = urlparse(url)
    return parsed_url._replace(scheme="").geturl().replace('//', '', 1)


def shorten_link(token, url, custom_domain):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': url,
               'domain': custom_domain}

    bitlink_response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    bitlink_response.raise_for_status()
    return bitlink_response.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'unit': 'day', 'units': '-1'}

    bitlink_response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
                                    headers=headers, params=params)
    bitlink_response.raise_for_status()
    return bitlink_response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': f'Bearer {token}'}

    bitlink_response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    return bitlink_response.ok


def validate_url(url):
    response = requests.get(url)
    response.raise_for_status()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Адрес сайта')

    return parser


def main():
    load_dotenv()
    access_token = os.getenv('BITLY_ACCESS_TOKEN')
    custom_domain = os.getenv('CUSTOM_DOMAIN')

    parser = create_parser()
    user_url = parser.parse_args().url

    validate_url(user_url)
    url_without_scheme = get_url_without_scheme(user_url)
    if is_bitlink(access_token, url_without_scheme):
        print(count_clicks(access_token, url_without_scheme))
    else:
        print(shorten_link(access_token, user_url, custom_domain))


if __name__ == '__main__':
    main()
