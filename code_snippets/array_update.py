def array_update(n, l):
    min_update = 1
    for ele in l:
        if ele * int(n) > sum(list(l)):
            min_update = ele
            break
    return min_update


n = int(input())
print(array_update(n, [x for x in range(n+1)]))