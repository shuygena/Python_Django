import sys

def prepare(words):
    toponyms = list(words.split(","))
    top_dict = dict()
    for top in toponyms:
        top = top.strip()
        if len(top) > 0:
            top_dict[top.title()] = top
    return (top_dict)
            


def print_list(words):
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
    toponyms = prepare(words)
    for top in toponyms:
        if top in states:
            print(capital_cities[states[top]], "is the capital of", top)
        elif top in capital_cities.values():
            for key in capital_cities:
                if (capital_cities[key] == top):
                    for state in states:
                        if (key == states[state]):
                            print(top, "is the capital of", state)
        else:
            print(toponyms[top], "is neither a capital city nor a state")

def search_by_key_or_value():
    if len(sys.argv) == 2:
        print_list(sys.argv[1])

if __name__ == '__main__':
    search_by_key_or_value()