import re
import chardet


def rm_webarch_stuff(path):
    new_string = str()
    with open(path, 'rb') as file:
        doc = file.read()
        doc = doc.decode(chardet.detect(doc)['encoding'])
    if re.findall(r'<head>[\w\W]+Include -->', doc):
        print('first')
        new_string = re.sub(r'<head>[\w\W]+Include -->', '<head>', doc, re.M)
    if re.findall(r'<script\stype=\"text/javascript\">\svar\sgaJs[\w\W]+</script>', doc):
        print('second')
        new_string = re.sub(r'<script\stype=\"text/javascript\">\svar\sgaJs[\w\W]+</script>', '', new_string, flags=re.M)
    if re.findall(r'<!--\n\s + [\w\W]+-->', new_string):
        print('third')
        new_string = re.sub(r'<!--\n\s + [\w\W]+-->', '', new_string, flags=re.M)
    if re.findall(r'/\*\n\s+[\w\W]+\*/', new_string):
        print('fourth')
        new_string = re.sub(r'/\*\n\s+[\w\W]+\*/', '', new_string, flags=re.M)

    with open(path, 'w') as file:
        file.write(new_string)


if __name__ == '__main__':
    rm_webarch_stuff('elgordo.ru/contacts.html')



