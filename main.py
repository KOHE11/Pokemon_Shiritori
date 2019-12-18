# -*- coding:utf-8 -*-
from tkinter import *
import ans_list
import tkinter.ttk as ttk
import time


#しりとりが続いていたら文字を下げる関数
def GetShiritori(y,done):
    if done != -1:
        y += 50 * done
        return y
    else:
        return done


#AIの答えを返す関数
def addRep(word):
    word = list(word)
    print(word)
    word_gobi = word[-1]
    for w in ans_list.word_list:
        if w[-1][-1] == 'ン':
            continue
        tmp = list(w)
        if word_gobi == tmp[0]:
            ans_list.word_list.remove(w)
            print(w)
            AIsay = "AI:" + w
            ListBox1.insert(END, AIsay)
            ListBox1.pack()
            if w[-1] == "ー":
                w = w[:-1]
            if w[-1] in ans_list.conv_dic:
                w = w + ans_list.conv_dic[w[-1]]
            word_list.append(w)
            return 1




def iskatahira(strj):
    return all([ch in katakana or ch in hiragana for ch in strj])



#入力したワードを取得
def GetWord():
    #入力が空白になってないかチェック
    if word_e.get()!='':
        word=str(word_e.get())
        return word
    else:
        ListBox1.insert(END, '文字を入力してね!')
        raise ValueError("文字を入力してね!")



#しりとりが成立しているかチェック
def check_siritori(word):
    global done, count
    done = 0
    count = 0
    #ワードを取得
    word=GetWord()
    #カタカナ・ひらがなをチェック
    if iskatahira(word):
        #最初のワードの場合
        if word_list==[]:
            word_list.append(word)
            count = 1
        #最初の文字としりとりの最後の文字が一致する場合
        elif word[0] == word_list[-1][-1]:
            if word in word_list:
                ListBox1.insert(END, 'それ前に使ったで?')
                raise ValueError("それ前に使ったよ?")

            if not word in ans_list.word_list:
                ListBox1.insert(END, 'そんな名前のポケモンはおらんで？')
                raise ValueError("そんな名前のポケモンはいないよ？")

            #lbl_p["text"] = word + '!'
            mysay = 'あなた: ' + word
            print(mysay)
            ListBox1.insert(END, mysay)
            ListBox1.pack()
            ans_list.word_list.remove(word)
            if word[-1] == "ー":
                word = word[:-1]
            if word[-1] in ans_list.conv_dic:
                word = word + ans_list.conv_dic[word[-1]]
            #リストにワードを追加
            word_list.append(word)

        else:
            ListBox1.insert(END, 'しりとりになってないよ！')
            raise ValueError("しりとりになってないよ!")

        #最後の文字が「ん」になっている場合
        if word[-1]=="ん" or word[-1]=="ン":
            ListBox1.insert(END, '「ン」がついちゃったね！')
            count = int(((len(word_list)+1) / 2) - 1)
            var = StringVar()
            var.set("あなたの記録：" + str(count) + "回")
            Counter = Label(textvariable=var, background='#FB1515', height=2)
            Counter.place(x=220, y=530)

            raise ValueError("「ン」がついちゃったね!")
        
    else:
        ListBox1.insert(END, 'もっかい入力してな！')
        raise ValueError("もう一度入力してね!")
    if addRep(word) == 1:
        print(len(word_list))
        print(count)
        print("addRep完了")
        print(word_list)

    word_e.delete(0, END)



if __name__=='__main__':
    #日本語チェック用
    hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんー"
    katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴ"

    #フィールド作成
    win=Tk()
    win.title('しりとりげええぇぇぇぇえむ')
    win.geometry('550x600')
    #done = 0  #しりとりが続いた回数
    frame = Frame(win, width=300, height=300, bg="white")
    frame.pack(padx=130, pady=100)

    #入力欄の設定
    word=0#入力欄に入れる文字
    word_e=Entry(win,width=25,font=('Verdana',10))#入力欄の設定
    word_e.place(x=130,y=50)#入力欄の位置
    word_list = ['AI: シリトリ']  #リスト、初期ワードの設定

    #リストボックス
    txt = StringVar(value=word_list)
    ListBox1 = Listbox(frame, listvariable=txt, width=100, height=200)
    ListBox1.insert(0, '「しりとり」の「り」からスタート!')
  

    #スクロールバーの生成・配置
    count = 0
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=ListBox1.yview)
    scrollbar.pack(fill='y', side='right')

    #ボタンの作成
    Button1 = Button(win, text='しりとり')
    Button1.bind("<Button-1>", check_siritori)
    Button1.place(x=125, y=0)
    ListBox1.pack()


    #カウンター用ボックス
    #count = int(len(word_list))
     


    #ボタンの作成
    Button2 = Button(win, text='おわり')
    Button2.bind("<Button-1>", sys.exit)
    Button2.place(x=250, y=0)

    win.mainloop()


