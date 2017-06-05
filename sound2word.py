# -*- coding: utf-8 -*-

import ConfigParser

import requests
import json
import os
import commands
#import time

#LISTEN_SECONDS = 5 
VOICE_IN_PATH = './tmp.flac'

# 録音
def listen(seconds):
    cmdline = 'AUDIODEV=hw:1 rec -c 1 -r 11025 ' + VOICE_IN_PATH + \
        ' trim 0 ' + str(seconds)
    os.system(cmdline)
    return os.path.getsize(VOICE_IN_PATH)

# 音声認識
def recognize():
    f = open(VOICE_IN_PATH, 'rb')
    voice = f.read()
    f.close()

    url = 'https://www.google.com/speech-api/v2/recognize?xjerr=1&client=chromium&'\
        'lang=ja-JP&maxresults=10&pfilter=0&xjerr=1&key=' + GOOGLE_APIKEY
    hds = {'Content-type': 'audio/x-flac; rate=11025'}

    try:
        reply = requests.post(url, data=voice, headers=hds).text
    except IOError:
        return '#CONN_ERR'
    except:
        return '#ERROR'

    objs = reply.split(os.linesep)
    for obj in objs:
        if not obj:
            continue
        alternatives = json.loads(obj)['result']

        if len(alternatives) == 0:
            continue
        return alternatives[0]['alternative'][0]['transcript']
    return ""


if __name__ == '__main__':
    #first time record will be failed. 
    listen(5)
    message = recognize().encode('utf-8')
    print(message)

    
