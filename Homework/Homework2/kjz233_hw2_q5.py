def split_parity(lst):
    ind = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            lst[i],lst[ind] = lst[ind],lst[i]
            ind += 1
    return lst

# lst = [1,2,3,3,4,5,2,2,2,3,4]
# print(split_parity(lst))
