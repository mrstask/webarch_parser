import ast
import json
from requests_html import HTMLSession


def get_all_urls():
    session = HTMLSession()
    r = session.get('https://web.archive.org/web/timemap/json?url=http%3A%2F%2Fwww.elgordo.ru/'
                    '&fl=timestamp:4,original,urlkey&matchType=prefix&filter=statuscode:200&filter='
                    'mimetype:video/x-flv&collapse=urlkey&collapse=timestamp:4&limit=100000')
    with open('response.txt', 'wb') as f:
        f.write(r.content)


def handle():
    with open('response.txt', 'r') as f:
        content = f.read()
    list_of_some = content
    anot_list = ast.literal_eval(list_of_some)
    anot_list = anot_list[1:]
    anot_set = set()
    for line in anot_list:
        anot_set.add(line[1])

    with open('set.txt', 'w') as f:
        f.write(json.dumps(list(anot_set)))