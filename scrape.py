from urllib import request
from bs4 import BeautifulSoup

l = []
for i in range(1, 894):
    i = str(i).zfill(3)
    print(i)
    url = 'https://zukan.pokemon.co.jp/detail/' + i
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "lxml")
    name = soup.find('title').get_text()
    response.close()
    name = name.split('｜')[0].split(" ")[0] 
    print(name)
    l.append(name + '\n')

with open('pk_list.txt', mode='w') as f:
    for i in range(len(l)):
        f.write(l[i])
