import requests

def start_search(filename):
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename)
    print(r.text)
    if r.text[:2] == 'We':
        return r.text
    else:
        start_search(r.text)

print('---------')
text = start_search('699991.txt')
print('---------')
print('---------')
print('-------')
