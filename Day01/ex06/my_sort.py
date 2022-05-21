def get_list(dict_years):
    list_years = list()
    for key in dict_years:
        list_years.append(key)
    list_years.sort()
    return(list_years)

def grammar_naci(d):
    dictionary = dict()
    for key in d:
        dictionary[d[key]] = list()
    for key in d:
        dictionary[d[key]].append(key)
    for key in dictionary:
        (dictionary[key]).sort()
    return(dictionary)

def dictionary_sorting():
    d={
    'Hendrix' : '1942', 'Allman' : '1946',
    'King' : '1925', 'Clapton' : '1945',
    'Johnson' : '1911', 'Berry' : '1926',
    'Vaughan' : '1954', 'Cooder' : '1947',
    'Page' : '1944', 'Richards' : '1943',
    'Hammett' : '1962', 'Cobain' : '1967',
    'Garcia' : '1942', 'Beck' : '1944', 'Santana' : '1947',
    'Ramone' : '1948', 'White' : '1975',
    'Frusciante': '1970', 'Thompson' : '1949',
    'Burton' : '1939', }
    new_dict = grammar_naci(d)
    list_years = get_list(new_dict)
    for year in list_years:
        for name in new_dict[year]:
            print(name)

if __name__ == '__main__':
    dictionary_sorting()