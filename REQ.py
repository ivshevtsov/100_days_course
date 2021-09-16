import requests

Home = 'https://stepic.org/media/attachments/course67/3.6.3'
r = requests.get(f'{Home}/699991.txt')


String = 'Hello'
print(String[:2])

while r.text[:2]!='We':
    r = requests.get(f'{Home}/{r.text}')
    print(r.text)

