import requests
import json
import random
import sys
import ans_list
from data import webhook_url

def send_message(message):
    """Summary line.

    slackの#pkチャンネルにメッセージを送信する

    Args:
        message (str): 送信したいメッセージ

    Returns:
        None

    """
    # Webhook URL
    url = webhook_url.url 

    # 送信メッセージ
    requests.post(url, data=json.dumps({'text':message}))

def pokemon(number):
    """Summary line.

    ポケモンの名前を返す

    Args:
        number (int): 名前を返す回数

    Returns:
        None

    """
    for i in range(number):
        random.shuffle(ans_list.word_list)
        send_message(ans_list.word_list[0])

if __name__=='__main__':
    pokemon(10)
    print("Sucess")