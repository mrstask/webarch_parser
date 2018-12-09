import json
from requests_html import HTMLSession
import requests
from yarl import URL
import os
import ast


class UrlTester:
    def __init__(self):
        self.good_urls = set()
        self.bad_urls = dict()
        self.response_code = int()
        self.session = HTMLSession()
        self.new_urls_dict = dict()
        self.domain = 'elgordo.ru'
        self.value = dict()
        self.page_url = str()

    def get_response_code(self):
        if self.value['real_url'] not in self.good_urls:
            if self.value['webarch_url'] not in self.bad_urls.keys():
                try:
                    self.response_code = self.session.get(self.value['real_url']).status_code
                    if self.response_code == 200:
                        print(self.value['real_url'], '200')
                        self.good_urls.add(self.value['real_url'])
                    else:
                        if self.value['webarch_url'] not in self.bad_urls.keys():
                            if self.value['webarch_url']:
                                print(self.value['real_url'], 'trying to download', self.value['webarch_url'])
                                self.download_missing()

                except requests.exceptions.SSLError:
                    self.response_code = 'SSLError'
                except requests.exceptions.ConnectionError:
                    self.response_code = 'ConnectionError'
                except Exception as e:
                    print(type(e))
                    self.response_code = str(e)
                self.new_urls_dict[self.value['real_url']] = {'page_url': self.page_url, 'webarch_url': self.value['webarch_url'],
                                                'response': self.response_code}
            else:
                self.new_urls_dict[self.value['real_url']] = {'page_url': self.page_url,
                                                              'webarch_url': self.value['webarch_url'],
                                                              'response': 404}
        else:
            self.new_urls_dict[self.value['real_url']] = {'page_url': self.page_url,
                                                      'webarch_url': self.value['webarch_url'],
                                                      'response': 200}

    def download_missing(self):
        response = self.save_file()
        if self.value['real_url'] in self.new_urls_dict.keys():
            self.new_urls_dict[self.value['real_url']][response] = response
        else:
            self.new_urls_dict[self.value['real_url']] = {'webarch_url': self.value['webarch_url'], 'response': response}
        if response == 200:
            self.good_urls.add(self.value['real_url'])
        elif response == 404:
            self.bad_urls[self.value['webarch_url']] = {'real_url': self.value['real_url'], 'response': response}

    def save_file(self):
        session = HTMLSession()
        try:
            response = session.get(self.value['webarch_url'])
            if response.status_code == 200:
                yarl_url = URL(self.value['real_url'].replace('?', '_'))
                path = self.domain + yarl_url.path
                if '.' in path:
                    path = path.replace('.', '_')
                directory = path.split('/')[:-1]
                directory = '/'.join(directory)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                with open(path, 'wb') as file:
                    file.write(response.content)
                print('downloaded', path)
                return response.status_code
            else:
                print('failed to download')
                self.bad_urls[self.value['webarch_url']] = {'real_url': self.value['real_url'], 'response': response}
                return response.status_code
        except Exception as e:
            print(type(e))
            return 'still nothing'

    def url_tester(self, urls_dict):
        for self.page_url, self.value in urls_dict.items():
            if self.value['real_url'].startswith('http://www.elgordo.ru'):
                self.get_response_code()
            elif self.value['real_url'].startswith('http://elgordo.ru'):
                self.value['real_url'] = self.value['real_url'].replace('http://elgordo.ru', 'http://www.elgordo.ru')
                self.get_response_code()
            elif self.value['real_url'].startswith('https://www.elgordo.ru'):
                self.value['real_url'] = self.value['real_url'].replace('https:', 'http:')
                self.get_response_code()
            elif self.value['real_url'].startswith('https://elgordo.ru'):
                self.value['real_url'] = self.value['real_url'].replace('https://', 'http://www.')
                self.get_response_code()
                self.new_urls_dict[self.page_url]['real_url'] = self.value['real_url']
            else:
                self.get_response_code()

    def good_and_bad_save(self):
        with open('good_urls.txt', 'w') as f:
            f.write(str(self.good_urls))
        with open('bad_urls.txt', 'w') as f:
            f.write(json.dumps(self.bad_urls))

    def good_and_bad_load(self):
        with open('good_urls.txt', 'r') as f:
            s = f.read()
            if s:
                self.good_urls = ast.literal_eval(s)
        with open('bad_urls.txt', 'r') as f:
            s = f.read()
            if s:
                self.bad_urls = json.loads(s)


if __name__ == '__main__':
    urltester = UrlTester()
    urltester.good_and_bad_load()
    urltester.url_tester(test_dict)
    urltester.good_and_bad_save()
    # print(urltester.new_urls_dict)
    # print(urltester.good_urls)
    # print(urltester.bad_urls)




    # with open('url_dict.txt', 'r') as f:
    #     urltester.urls_dict = json.loads(f.read())
    #
    # with open('url_dict_status.txt', 'w') as f:
    #     f.write(json.dumps(urltester.urls_dict))
    #     pprint(urltester.urls_dict)
    #
    # with open('good_urls.txt', 'w') as f:
    #     f.write(str(urltester.good_urls))
