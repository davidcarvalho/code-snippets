# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8, 9]
#
# set_l1 = set(l1)
# set_l2 = set(l2)
#
# if set_l1 & set_l2:
#     print(list(set_l1 & set_l2))

# x = [i for i in range(1, 10)]
# print(x)
#
# squares = [i if (i**2)%2 == 0 else 0 for i in x]
# print(squares)
#
# s1 = 'malayalam'
# s2 = 'radiz'
#
# def is_palindrome(s):
#     for i in range(0, len(s)//2):
#         print(s[i])
#         print(s[len(s) - i - 1])
#         if s[i] != s[len(s) - i - 1]:
#             return False
#     return True
#
# print(is_palindrome(s1))
# print(is_palindrome(s2))

# def fibonacci(num):
#     a = 0
#     b = 1
#     if num == 0:
#         return a
#     elif num == 1:
#         return b
#     else:
#         for i in range(2, num + 2):
#             c = a + b
#             a = b
#             b = c
#             print(b)
#         return b
#
# fibonacci(12)

# list
# tuple
# set
# dictionary

# list1 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
#
# uniq = []
# set1 = set()
#
# for e in list1:
#     if e not in set1:
#         set1.add(e)
#         uniq.append(e)
#
# print(uniq)
# print(set1)
#
# dupes = []
# seen = {}
#
# for x in list1:
#     if x not in seen:
#         seen[x] = 1
#     else:
#         dupes.append(x)
#         seen[x] += 1
#
# print(dupes)
# from collections import Counter
# list = [-20, 34, 21, -87, 92, 2147483647]
# dict = Counter(list)
# largest = max(dict.keys())
#
# print(largest)

# num = 1234567
# rev = 0
# while num > 0:
#     rev = (rev * 10) + (num % 10)
#     num = num // 10
#
# print(rev)

# num = 100
#
# def isPower2(num):
#     if num == 0:
#         return False
#     else:
#         while num != 1:
#             if num % 2 != 0:
#                 return False
#             num = num // 2
#     return True
# print(isPower2(num))