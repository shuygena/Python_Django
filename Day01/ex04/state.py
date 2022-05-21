import sys

def print_state(value):
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
    if value in capital_cities.values():
        for key in capital_cities:
            if (capital_cities[key] == value):
                for state in states:
                    if (key == states[state]):
                        print(state)
    else:
        print("Unknown capital city")
           
def search_by_value():
    if len(sys.argv) == 2:
        print_state(sys.argv[1])

if __name__ == '__main__':
    search_by_value() 
