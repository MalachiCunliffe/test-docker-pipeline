# fetch website
import requests
url = "http://google.com"


def fetch():
    r = requests.get(url)
    return r.text


print(fetch())
