def freq_dict(data):
    freq = {}
    for elem in data:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    return freq

print(freq_dict("Hello, how are you?"))
        
