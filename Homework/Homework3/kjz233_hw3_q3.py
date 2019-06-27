def find_duplicates(lst):
    d = {}
    for i in range(len(lst)):
        if lst[i] in d:
            d[lst[i]] += 1
        else:
            d[lst[i]] = 1
    print(d)

    return [elem for elem in d if d[elem] > 1]


lst=[2,4,4,1,2]
print(find_duplicates(lst))
