# def insertion_sort(lst):
#     for curr_index in range(1,len(lst)):
#         curr_num = lst[curr_index]
#         j = curr_index
#         while((j >= 1) and (lst[j-1] > curr_num)):    #the thing to the left is larger then
#             lst[j] = lst[j-1]   #switching the numbers # the number on the left moves one index to the right
#             j -= 1  #move the index one to the left
#             lst[j] = curr_num   #place the num where it belongs
#     print(lst)
#
# lst = [4,2,6,9,1,7,3]
#
# insertion_sort(lst)
#

def count_up(start,end):    #this prints it in increasing order because it hits the base case then works it way back up
    if (start == end):
        print(start)
    else:
        count_up(start,end-1)
        print(end)

count_up(1,10)

# def count_up(start,end):
#     if (start == end):
#         print(start)
#     else:
#         print(start)
#         count_up(start+1,end)
#
# count_up(1,10)

def count_up(start,end):
    if(start == end):
        print(start)
    else:
        mid = (start+end)//2
        count_up(start,mid)
        count_up(mid,end)
