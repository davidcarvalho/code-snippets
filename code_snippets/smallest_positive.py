
def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    smallest_postive_integer = 1
    for n in range(1,max(A)+2):
        if n not in set(A):
            smallest_postive_integer = n
            break
    return smallest_postive_integer
