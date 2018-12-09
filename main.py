import ast
from handlet import get_all_urls, handle
from timestamp_find import all_stuff, get_set_of_urls
# todo get all urls of site
get_all_urls()
# todo proccess urls with handler
handle()
# todo find timestamp for all urls
for url in ast.literal_eval(get_set_of_urls()):
    all_stuff(url)
