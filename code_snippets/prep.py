def list_search(lst, key):
    found = False
    if key in set(lst):
        found = True
    return found

print(list_search([1,2,3,4,5,6,7,8], 6))