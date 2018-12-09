import ast
import os
from requests_html import HTMLSession
from urllib.parse import urlencode
from yarl import URL
import json


def get_set_of_urls():
    with open('set.txt', 'r') as f:
        return f.read()


def all_stuff(url):
    domain = 'elgordo.ru'
    session = HTMLSession()
    yarl_url = URL(url)
    print(url)
    if '.flv' in url:
        path = domain+yarl_url.path
        directory = yarl_url.path.split('/')[:-1]
        directory = '/'.join(directory)
        directory = domain+directory
    else:
        print('gif')
        path = domain+yarl_url.path + '.html'
        directory = domain+yarl_url.path
    print(directory)

    url_encoded = urlencode({'url': url, 'collection': 'web', 'output':'json'})

    str_url = f'https://web.archive.org/__wb/sparkline?{url_encoded}'

    r = session.get(str_url)
    last_ts = json.loads(r.content)['last_ts']

    second_r = session.get(f'https://web.archive.org/web/{last_ts}/{url}')

    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'wb') as file:
        file.write(second_r.content)


if __name__ == '__main__':
    # url = ast.literal_eval(list_of_urls)[2]
    for url in ast.literal_eval(get_set_of_urls()):
        all_stuff(url)
