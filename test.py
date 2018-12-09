# import re
# import time
#
# t0 = time.time()
# content = 'https://web.archive.org/web/20150319200440/http://www.elgordo.ru:80/allresults.html'
# if re.match('^https:\/\/web\.archive\.org\/web\/\d{14}/', content):
#     print('sg')
#     new_string = re.sub('^https:\/\/web\.archive\.org\/web\/\d{14}/', '', content, flags=re.M)
# else:
#     new_string = re.sub('^https:\/\/web\.archive\.org\/web\/\d{14}\w{3}/', '', content, flags=re.M)
# t1 = time.time()
#
# total = t1-t0
# print(new_string)
# print(total)
#
# class Some:
#     def __init__(self):
#         self.sttt = '<meta content="text/html; charset=windows-1251" http-equiv="Content-Type"><link href="/web/20150925074252cs_/http://www.elgordo.ru:80/inc/css/reset.css" rel="stylesheet" type="text/css"><link href="/web/20150925074252cs_/http://www.elgordo.ru:80/inc/css/pages.css" rel="stylesheet" type="text/css"><link href="/web/20150925074252cs_/http://www.elgordo.ru:80/inc/css/lottery.css" rel="stylesheet" type="text/css"><link rel="shortcut icon" href="/web/20150925074252im_/http://www.elgordo.ru:80/img/favicon.ico"/>'
#         self.replace = '/web/20150925074252cs_/http://www.elgordo.ru:80/inc/css/reset.css'
#         self.replace_to = 'dfgdfgdfg'
#
#     def replacse(self):
#         self.sttt = self.sttt.replace(self.replace, self.replace_to)
#
# ssommne = Some()
#
#
# ssommne.replacse()
# print(ssommne.sttt)
value = 3
if value == 1 or value == 2:
    print('true')

import os
for path, subdirs, files in os.walk('elgordo.ru'):
    for name in files:
        if name.endswith('.html'):
            list_of_files.append(os.path.join(path, name))
print(list_of_files)