def solution(N):
    # write your code in Python 3.6
    binary = bin(N).replace('0b','')
    counter = 0
    if binary.count('1') == 1:
        counter = 0
    elif binary.count('0') == 0:
        counter = 0
    else:
        if binary[-1] == '1':
            counter = len(max(binary.split('1')))
        else:
            counter = len(max(binary.split('1')[:-1]))
    return counter


n = 328
print('{0:b}'.format(int(n)))
print(solution(n))