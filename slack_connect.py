# coding: utf-8
import requests
import time
import random
import ans_list

class SlackDriver:
    def __init__(self, _token):
        self._token = "xoxp-316938276210-654465000150-1020892209044-70ecb97ce93bdef61b1486d245331cf1"  # api_token
        self._headers = {'Content-Type': 'application/json'}
    def send_message(self, message, channel):
        params = {"token": self._token, "channel": channel, "text": message}
        r = requests.post('https://slack.com/api/chat.postMessage',
                          headers=self._headers,
                          params=params)
        print("return ", r.json())

if __name__ == '__main__':
    token = 'xoxb-316938276210-1008540058866-K0PKHmitrbFyOGlx3CElKduI'  # TODO your token.
    slack = SlackDriver(token)
    for i in range(10):
        random.shuffle(ans_list.word_list)
        slack.send_message(ans_list.word_list[i], "pk")
        time.sleep(1)
#https://qiita.com/stu345/items/24790710abc571aae3ea
#https://tadaken3.hatenablog.jp/entry/python-slack