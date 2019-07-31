import config
from aip import AipSpeech
from moviepy.editor import *
from moviepy.audio.fx import all
import os

def get_text():
    text_list = []
    with open('data.txt', "r", encoding='utf-8', errors='ignore') as f:
        for string in f.readlines():
            text_list.append(string)
    return text_list


def get_radio(text, i):
    client = AipSpeech(config.APP_ID, config.API_KEY, config.SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'spd': 3,
        'vol': 10,
        'pit': 4,
        'per': 3
    })
    if not isinstance(result, dict):
        with open('auido/auido_%s.mp3' % str(i), 'wb') as f:
            f.write(result)




