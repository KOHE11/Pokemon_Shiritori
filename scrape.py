from urllib import request
from bs4 import BeautifulSoup

l = []
for i in range(1, 891):
    i = str(i).zfill(3)
    print(i)
    url = 'https://zukan.pokemon.co.jp/detail/' + i
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "lxml")
    name = soup.find('title').get_text()
    response.close()
    print(name.split('｜')[0])
    l.append(name.split('｜')[0] + '\n')

with open('pk_list.txt', mode='w') as f:
    for i in range(len(l)):
        f.write(l[i])