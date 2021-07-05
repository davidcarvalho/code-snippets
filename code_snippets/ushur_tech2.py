str1 = 'emocleWoTruhsU'
str2 = 'yMemaNsIdivaD'

expected_str = 'Welcome To Ushur'


# def split_reverse(str2):
#     splitter = 'oT'
#     reversed = []
#
#     for word in str2.split(splitter):
#         reversed.append(word[::-1])
#
#     reversed.insert(1, splitter[::-1])
#     print(' '.join(reversed))


def split_reverse(str2):
    temp_str = ''
    temp_lst = []
    for i in str2:
        temp_str += i
        if i.isupper():
            temp_lst.append(temp_str[::-1])
            temp_str = ''
    print(' '.join(temp_lst))

split_reverse(str1)

split_reverse(str2)