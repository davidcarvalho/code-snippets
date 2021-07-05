s = 'abcda'


def longest_substring(s):
    l = []
    for i in range(0, len(s)):
        if not is_duplicate(s[i:]):
            l.append(s[i:])
        for j in range(i+1, len(s)):
            if not is_duplicate(s[i:j]):
                l.append(s[i:j])
    print(l)
    l.sort(reverse=True, key=len)
    print(len(l[0]))


def is_duplicate(string):
    test_dict = {}
    for c in string:
        if c in test_dict:
            return True
        else:
            test_dict[c] = ''
    return False

longest_substring(s)