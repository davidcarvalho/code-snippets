def solution(A):
    # write your code in Python 3.6
    dct = {}
    counter = 1
    for i in A:
        if i in dct:
            counter += 1
        dct[i] = counter
        # reset counter
        if counter == 2:
            counter = 1
    for k, v in dct.items():
        if v == 1:
            return k


# print(solution([1,1,2,2,3,3,4,4,5]))
def new(A):
    temp_str = ''.join([str(ele) for ele in A])
    for i in A:
        if len(temp_str.split(str(i))) == 2:
            return i
        # print(len(''.join(A).split(str(i))))

new([1,1,2,2,3,3,4,4,5])