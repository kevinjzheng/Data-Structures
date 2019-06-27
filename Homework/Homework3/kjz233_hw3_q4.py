# def remove_all(lst,value):
#     end = False
#     while(end==False):
#         try:
#             lst.remove(value)
#         except ValueError:
#             end = True

def remove_all(lst,value):
    lst[:] = [num for num in lst if num != value]
    return lst

# lst = [1,2,3,4,1,1,2,4]
# print(remove_all(lst,2))
