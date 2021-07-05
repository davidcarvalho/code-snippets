lst = [ 2, 4, 3, 5, 6 , 1, 0, 8, 9 ]
sum1 = 9

def sum_pairs(lst, sum_of_numbers):
    new_list=[]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            new_list.append((lst[i], lst[j]))
    print(new_list)

    for index, pair in enumerate(new_list):
        if sum(pair) == sum_of_numbers:
            print(new_list.pop(index))


sum_pairs(lst, sum1)

