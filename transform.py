import re

def trans_word(word):
    if (len(re.findall(r'^[{ァ-ヶ|ー}]+$', word)) != 1):
        trans_dic = {'・' : '', '・' : '', '：' : '', '♂' : 'オス', '♀' : 'メス', '２' : 'ツー', 'Z' : 'ゼット'}
        for k, v in trans_dic.items():
            word = word.replace(k, v)
    return word

if __name__=='__main__':
    f = open('pk_list.txt', 'r')
    l = f.readlines()
    for w in l:
        trans_word(w.replace('\n', ''))