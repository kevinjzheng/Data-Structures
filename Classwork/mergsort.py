def merge(lst,low_left,high_left,high_right):
    low_right = high_left + 1
    i_left = low_left
    i_right = low_right
    merged_list = []
    while (i_left <= high_left) and (i_right <= high_right):
        if lst[i_left] < lst[i_right]:
            merged_list.append(lst[i_left])
            i_left += 1
        else:
            merged_list.append(lst[i_right])
            i_right += 1
    while (i_left <= high_left):
        merged_list.append(lst[i_left])
        i_left += 1
    while (i_right <= high_right):
        merged_list.append(lst[i_right])
        i_right += 1
    for i in range(len(merged_list)):
        lst[low_left+i] = merged_list[i]

def merge_sort(lst):
    if len(lst) == 0:
        return
    else:
        merge_sort_helper(lst,0,len(lst)-1)

def merge_sort_helper(lst,low,high):
    if low == high:
        return
    else:
        mid = (low + high) // 2
        merge_sort_helper(lst,low,mid)
        merge_sort_helper(lst,mid+1,high)
        merge(lst,low,mid,high)

lst = [1,4,6,7,213,2,352,34,6,0]
merge_sort(lst)
print(lst)
