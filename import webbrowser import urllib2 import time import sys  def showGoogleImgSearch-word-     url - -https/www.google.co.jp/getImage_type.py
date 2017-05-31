import webbrowser
import time
import sys

def showGoogleImgSearch(word):
    url = "https://www.google.co.jp/search?q=" + word + "&tbm=isch"
    webbrowser.open(url, new=0)

if __name__ == "__main__":
    
    print "\ntype 'thank you has' if you want to stop\n"
    while(1):
        print "type a word please: "
        input_word = sys.stdin.readline()
        if input_word == "thank you has\n":
            print "\nYou're welcome, see you again!\n"
            break
        showGoogleImgSearch(input_word)
        time.sleep(2)
