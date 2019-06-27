def find_lst_max(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        rest = find_lst_max(lst[1:])
        if lst[0] > rest:
            return lst[0]
        return rest

print(find_lst_max([1,2,3,4,5,100,12,2]))
print(find_lst_max([]))

# def product_evens(lst,n):
#     if len(lst) == 0:
#         return None
#     if len(lst) == 1:
#         if (lst[0] < n) and (lst[0] % 2 == 0):
#             return lst[0]
#     else:
#         rest = product_evens(lst[1:],n)
#         if (lst[0] < n) and (lst[0] % 2 == 0):
#             return rest * lst[0]
#         return rest
#
# lst = [1,2,3,4,5,100,12,2]
# lst = [1]
# print(product_evens(lst,len(lst)))

# def is_palindrome(input_str,low,high):
#     if low >=  high:
#         return True
#     else:
#         rest = is_palindrome(string,low+1,high-1)
#         if string[low] == string[high]:
#             return rest
#         return False
#
# # string = 'kayak'
# # string = 'pythop'
# # string = "racecar"
# print(is_palindrome(string,0,(len(string)-1)))
#
# def binary_search(srt_lst,val,low,high):
#     if len(srt_lst) == 0:
#         return None
#     else:
#         mid = (low+(high))//2
#         if val > srt_lst[mid]:
#             low = mid
#             rest = binary_search(srt_lst,val,low+1,high)
#             return rest
#         elif val < srt_lst[mid]:
#             high = mid
#             rest = binary_search(srt_lst,val,low,high)
#             return rest
#         return mid
#
# lst = [1,2,30,32,35,40,56,57,69,79,88,99,100]
# print(binary_search(lst,40,0,(len(lst)-1)))

# import os
#
# def disk_usage(path):
# # our base case is when it is a file because that means there no more paths downwards
#     total = os.path.getsize(path)
#     if os.path.isdir(path):
#         for item in os.listdir(path):
#             newPath = os.path.join(path,item)
#             #print(newPath)
#             total += disk_usage(newPath)
#             #print(item)
#     print(path, ':', total)
#     return total
#
# print(disk_usage("/Users/lightning/Desktop/Lab5"))
#
# # print(os.path.getsize("/Users/lightning/Desktop/Lab5/text.txt"))
# # print(os.path.isdir("/Users/lightning/Desktop/Lab5/"))
# # print(os.listdir("/Users/lightning/Desktop/Lab5/"))
# # print(os.path.join("/Users/lightning/Desktop/","Lab5.py"))
