# lst = [1,2,3]
#
# for elem in lst:
#     elem += 10
#
# print(lst)
#
# for ind in range(len(lst)):
#     lst[ind] = lst[ind]+10
#
# print(lst)
#
# lst1 = [1,2,3]
# lst2 = lst1
# lst3 = [1,2,3]
# lst1.append(4)
# lst2.append(5)
# lst3.append(6)
# print(lst1)
# print(lst2)
# print(lst3)

#list constructor
# lst4 = list('abc')
# print(lst4)

# lst1 += lst2 does not equal lst1 = lst1 + lst2 because the "+" operator
# constructs a new list while the "+=" mutates the list
#
# def main():
#     lst = [1,2,3]
#     s = "abc"
#     func(lst,s)
#     print("main: lst=",lst,"s =",s)
# def func(lst,s): # this refers to the same lst and s created therefore editing it
#                 # here would change the lst and the s created in main
#     for ind in range(len(lst)):
#         lst[ind] += 10
#     lst.append(4)
#     s.upper()
#     print("func: lst =",lst,"s =",s)
# main()
#
# lst5 = [1,2,3,4,5]
# lst6 = lst5.copy()
# lst6[0] = 10
# print(lst5)
# print(lst6)
#
# lst7 = [1,[2,3],[4,5]]
# lst8 = lst7.copy()
# lst8[0] = 10
# lst8[1][0] = 20
#
# print(lst7)
# print(lst8)
# # it took the change of the 20 in the index because the list is mutable and the original reference was affected as well

import copy
#
# lst1 = [1,[2,3],[4,5]]
# lst2 = copy.deepcopy(lst1)
# lst2[0] = 10
# lst2[1][0] = 20
# print(lst1)
# print(lst2)

lst1 = [1,[2,3],[4,5]]
lst2 = copy.copy(lst1)
lst2[0] = 10
lst2[1][0] = 20
print(lst1)
print(lst2)
