def split_by_sign(lst,low,high):
    if low == high:
        return
    else:
        if lst[low] > 0 and lst[high] < 0:
            lst[low],lst[high] = lst[high],lst[low]
            split_by_sign(lst,low+1,high)
        elif lst[low] > 0 and lst[high] > 0:
            split_by_sign(lst,low,high-1)
        elif lst[low] < 0 and lst[high] > 0:
            split_by_sign(lst,low+1,high-1)
        elif lst[low] < 0 and lst[high] < 0:
            split_by_sign(lst,low+1,high)




# lst = [1,2,-1,2,-2,3,-4,5,-3,6,1,2,-3]
# (split_by_sign(lst,0,len(lst)-1))
# print(lst)
