def print_dict(dictionary):
    for key in dictionary:
        print(key, ":", dictionary[key])
        # for name in dictionary[key]:
        #     print(key, ":", name)

def grammar_naci(d):
    dictionary = dict()
    for element in d:
        dictionary[element[1]] = str()
    for element in d:
        dictionary[element[1]] += element[0] + ' '
    return(dictionary)    

def translator():
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
        ]
    new_dict = grammar_naci(d)
    print_dict(new_dict)

if __name__ == '__main__':
    translator()