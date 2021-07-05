str = 'Java is a good programming language'
st2 = 'Jiagpl'

temp = str.split(" ")
exp_str = ''

for i in temp:
    exp_str += i[0]

print(exp_str)

# Define two dictionaries , join them and print the new joined dictionary
d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}

for key in d2.keys():
    d1[key] = d2[key]

print(d1)

