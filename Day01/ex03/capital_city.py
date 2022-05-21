import sys

def print_capital(key):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if key in states:
        print(capital_cities[states[key]])
    else:
        print("Unknown state")
 
def key_search():
    if len(sys.argv) == 2:
        print_capital(sys.argv[1])

if __name__ == '__main__':        
    key_search()