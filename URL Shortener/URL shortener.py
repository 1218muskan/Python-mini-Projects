#pip intall pyshorteners
from pyshorteners import Shortener
api_key = ""

def shorten_url():
    shortener = Shortener(api_key = api_key)  #invoking constructor
    long_url = input("Enter the URL to shorten: ")
    short_url = shortener.bitly.short(long_url)

    print(short_url)

def expand_url(short_url):
    shortener = Shortener(api_key = api_key)
    Long_url = shortener.bitly.expand(short_url)
    print(Long_url)


shorten_url()  #calling function
