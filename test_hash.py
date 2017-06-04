#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os
import commands
import time
import webbrowser

GOOGLE_APIKEY = 'Your_Google_API_KEY'

LISTEN_SECONDS = 5 
VOICE_IN_PATH = './tmp.flac'

# 録音
def listen(seconds):
#    print('lestening...')
    cmdline = 'AUDIODEV=hw:1 rec -c 1 -r 11025 ' + VOICE_IN_PATH + \
        ' trim 0 ' + str(seconds)
    os.system(cmdline)
    return os.path.getsize(VOICE_IN_PATH)
    
# 音声認識
def recognize():
#    print('recognizing...')    
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


def current_milli_time():
    return int(round(time.time() * 1000))

if __name__ == '__main__':
    #first time record will be failed. 
    listen(1)
    no_word = 0
    wifi_err = 0
    
try:
    while True:
        # 録音
        t0 = current_milli_time()          
        size = listen(LISTEN_SECONDS)
        t = current_milli_time() - t0
        if (t < 2000):
            print('USB microphone not available')
            time.sleep(10)
            continue
 #       print('listened:' + str(t) + 'ms')
 #       print('voice data size=' + str(size))
        
        # 音声認識
        t0 = current_milli_time()
        message = recognize().encode('utf-8')
 #       print('recognized:' + str(current_milli_time() - t0) + 'ms')
        if (message == '#CONN_ERR'):
            print('internet not available')
            time.sleep(10)
            continue
        elif (message == '#ERROR'):
            print('voice recognize failed')
            time.sleep(10)
            continue  
        else :
            print( message )
            if (message!='') :
                url = "https://www.google.co.jp/search?q=" + message + "&tbm=isch"
                webbrowser.open(url)

except KeyboardInterrupt:
    pass
