import sys
import requests
import json
import dewiki

def make_wiki():
    if len(sys.argv) != 2:
        print("Error: wrong number of arguments")
        exit()
    try:
        URL = "https://en.wikipedia.org/w/api.php"
        page = sys.argv[1]
        PARAMS = {
            "action": "parse",
            "page": page,
            "format": "json",
            "prop": "wikitext",
            "redirects": True
        }
        req = requests.Session().get(url=URL, params=PARAMS)
        res = dewiki.from_string(req.json()["parse"]["wikitext"]["*"].replace("\n\n", "\n"))
        f = open(dewiki.from_string(page).replace(" ", "_") + ".wiki", "w+")
        f.write(res)
    except Exception as ex:
        print("Error:", ex)

if __name__ == '__main__':
    make_wiki()

# python3 -m venv local_lib
# source local_lib/bin/activate

# pip3 install  -r requirement.txt
