def solution(A, K):
    # write your code in Python 3.6
    lst = [0] * len(A)
    for count, item in enumerate(A):
        if count + K > len(A) - 1:
            lst[(count + K) % len(A)] = item
        else:
            lst[count + K] = item
    return lst


print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
