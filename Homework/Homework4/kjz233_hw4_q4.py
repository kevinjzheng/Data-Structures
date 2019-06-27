def list_min(lst,low,high):
    if low == high:
        return lst[low]
    else:
        rest = list_min(lst,low+1,high)
        if lst[low] < rest:
            return lst[low]
        return rest

# lst = [200,3,2,15,23,1,5]
# print(list_min(lst,0,len(lst)-1))
