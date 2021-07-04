# tuple1 = ('this', 'is', 'a', 'bot', 'which', 'does', 'things')
#
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# print(list(map(lambda x: x * 2, li)))
# first = [1, 2, 3, 4, 5]
# second = first
# second.append(6)
# print(first)
# print(second)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[-1:-5:-1])

listA = [1, 2, 3]
def funcA(listA):
    listA = listA * 2
    return None

funcA(listA)
print(listA) # print Statement 1

listB = [1, 2, 3]
def funcB(listB):
    listB=listB.extend([1, 2, 3])
    return None

funcB(listB)
print(listB) # print Statement 2