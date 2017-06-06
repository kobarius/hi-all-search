# hi-all-search

search all you say

## Usage
 1. 音声データ操作用にsox（Sound eXchange）ライブラリをインストール
```
$ sudo apt-get install alsa-utils sox libsox-fmt-all
```
 2. 「congfig.ini」でGoogle SpeechのAPIキーを指定
```
GOOGLE_API_KEY = Set_Your_Google_API_KEY
```
 3. 実行
```
$ python hash.py
```

## Requirement
- OS：Linux（Raspbian,Ubuntuで動作確認済）
- Python：3.x系（2系では動きません）
