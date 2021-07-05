def dict_print(dict1):
    for key in dict1.keys():
        if type(dict1[key]) is dict:
            dict_print(dict1[key])
        else:
            print(f'Dictionary key {key} for dictionary value {dict1[key]}')


d = {x: x ** 2 for x in [2, 3, 4, 5, 6, 7]}
print(d)
dict_print(d)
