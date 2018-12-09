import os
from get_links import GetLinks
from url_tester import UrlTester
from url_replace import UrlReplace
from shit_cleaner import rm_webarch_stuff
domain = 'elgordo.ru'
list_of_files = list()
for path, subdirs, files in os.walk('elgordo.ru'):
    for name in files:
        if name.endswith('.html'):
            list_of_files.append(os.path.join(path, name))
get_links = GetLinks()
urltester = UrlTester()
url_replace = UrlReplace()
for file in list_of_files:
    print(file)
    # get urls from page
    # opening file
    get_links.open_html_file(file)
    # finding links
    get_links.find_a_links()
    get_links.html_find_lookalike_links()
    # cleaning links
    for link in get_links.links:
        get_links.result_dict[link] = get_links.get_real_urls(link)
    # check live urls
    # test live urls and download dead
    urltester.good_and_bad_load()
    urltester.url_tester(get_links.result_dict)
    urltester.good_and_bad_save()
    # todo if dead url downloaded add to queue
    # todo replace urls
    url_replace.file_open(file)
    print(urltester.new_urls_dict)
    url_replace.replace_urls(urltester.new_urls_dict, domain)
    # url_replace.replace_charset()
    url_replace.file_save()
    # todo remove webarchive stuff
    rm_webarch_stuff(file)

# todo save all html_files to database
# todo update url replacer to replace all urls by regex, not by list
# todo all new links that`re on page add to database
# todo save all to github
# todo for new urls create table in database where all links to this urls are stored
# todo download asycnronously all new urls