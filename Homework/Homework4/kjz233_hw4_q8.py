def flat_list(nested_lst,low,high):
    flatLst = []
    nested_lst = nested_lst[low:high+1]
    for elem in nested_lst:
        if not isinstance(elem,list):
            flatLst.append(elem)
        else:
            flatLst.extend(flat_list(elem,0,len(elem)-1))
    return flatLst

# nested_lst = [[1,2],3,[4,[5,6,[7],8]]]
# print(flat_list(nested_lst,0,1))
# print(flat_list(nested_lst,0,len(nested_lst)-1))
