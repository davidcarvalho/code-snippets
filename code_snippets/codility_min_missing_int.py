def solution(list1):
    temp = False
    # write your code in Python 3.6
    list1 = sorted(list1)
    dict1 = {e: '' for e in list1}
    print(dict1)
    for i in range(1, max(list1)+2):
        if i not in dict1:
            temp = i
            break
    if not temp:
        temp = 1
    return temp

x = solution([1, 3, 6, 4, 1, 2])
assert x==5, f'x is {x}'
x = solution([1, 2, 3, ])
assert x==4, f'x is {x}'
x = solution([-1, -2, -4])
assert x==1, f'x is {x}'
