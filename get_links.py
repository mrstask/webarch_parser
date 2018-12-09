from lxml import html as lhtml
import re
import chardet
import json


class GetLinks:
    def __init__(self):
        self.links = set()
        self.result_dict = dict()
        self.domain = 'http://elgordo.ru'
        self.doc = str()
        self.webarch_url = str()
        self.real_url = str()

    def open_html_file(self, path):
        with open(path, 'rb') as file:
            self.doc = file.read()
            self.doc = self.doc.decode(chardet.detect(self.doc)['encoding'])

    def find_a_links(self):
        a_links = lhtml.fromstring(self.doc)
        a_links = a_links.xpath('//a/@href')
        [self.links.add(link) for link in a_links]

    def html_find_lookalike_links(self):
        match = re.findall(r'=[\'\"]?((http|/)[^\'\" >]+)', self.doc)
        [self.links.add(x[0]) for x in match]

    def html_find_css_links(self):
        match = re.findall(r'r"url\((.*?)\)"', self.doc)
        [self.links.add(x[0]) for x in match]

    def rm_webarch(self, wrch_url):
        if re.match('^https:\/\/web\.archive\.org\/web\/\d{14}/', wrch_url):
            clean_url = re.sub('^https:\/\/web\.archive\.org\/web\/\d{14}/', '', wrch_url, flags=re.M)
        else:
            clean_url = re.sub('^https:\/\/web\.archive\.org\/web\/\d{14}\w{3}/', '', wrch_url, flags=re.M)
        return clean_url

    def get_real_urls(self, url):
        if url.startswith('/'):
            if url.startswith('//'):
                self.webarch_url = 'https:' + url
                self.real_url = self.rm_webarch(self.webarch_url)
            elif url.startswith('/web/'):
                self.webarch_url = 'https://web.archive.org' + url
                self.real_url = self.rm_webarch(self.webarch_url)
            else:
                self.webarch_url = ''
                self.real_url = self.domain + url
        elif url.startswith('http'):
            if url.startswith('https://web.archive.org/web/'):
                self.webarch_url = url
                self.real_url = self.rm_webarch(url)
        else:
            self.webarch_url = ''
            self.real_url = self.domain+url
        return {'webarch_url': self.webarch_url, 'real_url': self.real_url}


if __name__ == '__main__':
    get_links = GetLinks()
    # opening file
    get_links.open_html_file('rules.html')
    # finding links
    get_links.find_a_links()
    get_links.html_find_lookalike_links()
    # cleaning links
    for link in get_links.links:
        get_links.result_dict[link] = get_links.get_real_urls(link)
    print(get_links.result_dict)

    # doc = open_html_file('rules.html')
    # find_a_links(links_main, doc)
    # html_find_lookalike_links(links_main, doc)
    # for link in links_main:
    #     dict_main[link] = get_real_urls(link, domain)
    # print(dict_main)
    # with open('url_dict.txt', 'w') as f:
    #     f.write(json.dumps(dict_main))