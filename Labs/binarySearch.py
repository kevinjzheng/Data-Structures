def binarySearch(L, x):
    # base cases
    if L == []:
        return False
    if len(L) == 1:
        return L[0] == x

    # 1. Check the median.
    mid = len(L) // 2
    if x == L[mid]:
        return True

    # recursive cases
    # 2
    elif x < L[mid]:
        return binarySearch(L[:mid], x) # assume this just works
    # 3
    else: # x > L[mid]
        return binarySearch(L[mid+1:], x) # assume this just works


A = list(range(100))
print(binarySearch(A, 15)) # --> True
