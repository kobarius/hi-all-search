# -*- coding: utf-8 -*-

import configparser

# --- from Other File
from getAPIkey import getAPIkey
from listen import sound2word
from recognize import sound2word
from showGoogleImgSearch import getImage


def hash():
    inifile = configparser.ConfigParser()
    inifile.read('./config.ini')
    API_KEY = inifile['settings']['GOOGLE_API_KEY']
    VOICE_IN_PATH = inifile['settings']['VOICE_IN_PATH']
    LISTEN_SECONDS = inifile['settings']['LISTEN_SECONDS']

    DefStr = 'Set_Your_Google_API_KEY'
    EnvName = 'GOOGLE_API_KEY'

    API_KEY = getAPIkey(API_KEY,DefStr,EnvName)

    try:
        while True:
            listen(5,VOICE_IN_PATH)
            message = recognize(API_KEY,VOICE_IN_PATH).encode('utf-8')
            print(message.decode('utf-8'))

            if(message!=''):
            showGoogleImgSearch(message)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
	hash()

