import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/819.txt')

print(len(r.text.splitlines()))

