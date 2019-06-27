import DoublyLinkedLists

lnk_lst2 = DoublyLinkedLists.DoublyLinkedList()
lnk_lst2.add_first(20)
lnk_lst2.add_last(40)

lnk_lst1 = DoublyLinkedLists.DoublyLinkedList()
lnk_lst1.add_first(2)
lnk_lst1.add_last(4.0)
lnk_lst1.add_last([5,3,6])
lnk_lst1.add_last(lnk_lst2)

print(lnk_lst1)

def remove_all(lnk,lst,item):
    if lnk_lst.is_empty():
        return
    cursor = lnk_lst.first_node()
    while cursor is not lnk.lst.trailer:
        if cursor.data == item:
            next_node = cursor.next
            lnk_lst.delete_node(cursor)
            cursor = next_node
        else:
            cursor = cursor.next

def max_in_lnk_lst(lnk_lst):
    if lnk_lst.is_empty():
        raise Exception('Empty sequence has no max')
    return max_in_lnk_sublist(lnk_lst,lnk_lst.first_node())

def max_in_lnk_sublist(lnk_lst,sublist_head):
    if sublist_head.next is lnk_lst.trailer:
        return sublist_head.data
    else:
        rest_max = max_in_lnk_sublist(lnk_lst,sublist_head.next)
        return max(rest_max,sublist_head.data)
# def max_in_lnk_lst(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         rest = max_in_lnk_lst(lst[1:])
#         return max(rest,lst[0])
def average_compression(lnk_lst,k):
    if lnk_lst.is_empty():
        raise Exception('Empty sequence has no average')
    cursor = lnk_lst.first_node()
    while cursor is not lnk_lst.trailer:
        curr_sum = 0
        for i in range(k):
            curr_sum += cursor.data
            next_node = cursor.next
            lnk_lst.delete_node(cursor)
            cursor = next_node
        curr_avg = curr_sum / k
        lnk_lst.add_before(cursor,curr_avg)
