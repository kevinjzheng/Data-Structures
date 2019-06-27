def permutations(lst,low,high):
    if low == high:
        return [[lst[low]]]
    newLst = []
    for i in range(low,high+1):
        lst[low],lst[i] = lst[i],lst[low]
        for other in permutations(lst,low+1,high):
            part = [lst[low]] + other
            newLst.append(part)
        lst[low],lst[i] = lst[i],lst[low]
    return newLst

# lst = [1,2,3]
# print(permutations(lst,0,len(lst)-1))
