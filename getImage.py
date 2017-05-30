import webbrowser
import urllib2
import time

def showGoogleImgSearch(word):
    url = "https://www.google.co.jp/search?q=" + word + "&tbm=isch"
    webbrowser.open(url, new=0)

if __name__ == "__main__":
    showGoogleImgSearch("robot")
    time.sleep(3)

    showGoogleImgSearch("python")
    time.sleep(3)

    showGoogleImgSearch("tomato")
    time.sleep(3)

    showGoogleImgSearch("noodle")
    time.sleep(3)



