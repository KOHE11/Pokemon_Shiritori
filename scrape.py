from urllib import request
from tqdm import tqdm
from bs4 import BeautifulSoup
import time
import transform

def scrape_pk(pk_num):
    l = []
    bar = tqdm(total=pk_num)
    bar.set_description('Progress')
    for i in range(pk_num):
        i = str(i).zfill(3)
        url = 'https://zukan.pokemon.co.jp/detail/' + str(int(i) + 1)
        response = request.urlopen(url)
        soup = BeautifulSoup(response, "lxml")
        name = soup.find('title').get_text()
        response.close()
        name = name.split('｜')[0].split(" ")[0]
        name = transform.trans_word(name)
        l.append(name + '\n')
        bar.update(1)

    with open('pk_list.txt', mode='w') as f:
        for i in range(len(l)):
            f.write(l[i])

if __name__=='__main__':
    scrape_pk(898)
