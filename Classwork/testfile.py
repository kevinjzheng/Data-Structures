# def example3(n):
#     i = 1
#     sum = 0
#     while (i< n*n):
#         i *= 2
#         sum += i
#     return sum
#
# print(example3(10000000))
#
#
# def is_sorted(lst,low,high):
#     if low == high:
#         return True
#     else:
#         rest = is_sorted(lst,low,high-1)
#         if lst[high-1] < lst[high]:
#             return rest
#         else:
#             return False
#
# lst = [1,3,6,4,12,15,31]
# print(is_sorted(lst,0,len(lst)-1))
#
# def is_sorted(lst,low,high):
#     if low == high:
#         return True
#     else:
#         rest = is_sorted(lst,low+1,high)
#         if lst[low] < lst[low+1]:
#             return rest
#         else:
#             return False
#
# lst = [1,3,6,4,12,15,31]
# print(is_sorted(lst,0,len(lst)-1))

# def remove_all_evens(lst):
#     even = 0
#     for i in range(len(lst)):
#         if lst[i] % 2 != 0:
#             lst[even] = lst[i]
#             even += 1
#     for i in range(even,len(lst)):
#         lst.pop()
#
# lst = [2,3,5,2,16,13]
# remove_all_evens(lst)
# print(lst)

# def find_all(lst,low,high,elem):
#     if low == high:
#         if lst[low] == elem:
#             return [low]
#         else:
#             return []
#     else:
#         rest = find_all(lst,low+1,high,elem)
#         if lst[low] == elem:
#             return [low] + rest
#         return rest
#
# lst = [7,3,2,4,2,1,1,2,5,0]
# print(find_all(lst,3,8,2))
#
# def words_keep_numbers_flip(lst):
#     ind = 0
#     n = len(lst) - 1
#     for i in range(len(lst)):
#         if isinstance(lst[i],str):
#             lst[ind],lst[i] = lst[i],lst[ind]
#             ind += 1
#     while ind <= (n):
#         lst[ind],lst[n] = lst[n],lst[ind]
#         ind += 1
#         n -= 1
# lst = ["keep",3,'this','order',2,1]
# words_keep_numbers_flip(lst)
# print(lst)

lst = [1,2,3]
# print(lst[1::-1])
print(lst.max())
