import sys
from antigravity import geohash

def check_datedow(str, strerror):
    dl = str.split("-")
    if (len(dl) != 4):
        print("Error: datedow type isn't correct" + strerror)
        sys.exit()
    if(dl[0].isdigit() == False and len(dl[0]) != 4
    and dl[1].isdigit() == False and len(dl[1]) != 2
    and dl[2].isdigit() == False and len(dl[2]) != 2):
        print("Error: datedow type isn't correct" + strerror)
        sys.exit()
        return(dl[3])

def hashing():
    strerror = ("""
Usage: python3 {0} [latitude] [longtitude] [datedow]
Example: python3 {0} 37.421542 -122.085589 2005-05-26-10458.68""").format(sys.argv[0])
    if (len(sys.argv) != 4):
        print("Error: wrong number of arguments" + strerror)
        sys.exit()
    try:
        lat = float(sys.argv[1])
    except Exception:
        print("Error: latitude type isn't float" + strerror)
        sys.exit()
    try:
        log = float(sys.argv[2])
    except Exception:
        print("Error: longtitude type isn't float" + strerror)
        sys.exit()
    try:         
        dd = sys.argv[3].encode("UTF-8")
        float(check_datedow(sys.argv[3], strerror))
    except Exception:
        print("Error: datedow type isn't correct" + strerror)
        sys.exit()
    geohash(lat, log, dd)

if __name__ == '__main__':
    hashing()
    