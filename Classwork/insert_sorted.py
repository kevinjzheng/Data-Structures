import DoublyLinkedLists

lnk_lst = DoublyLinkedLists.DoublyLinkedList()
lnk_lst.add_last(1)
lnk_lst.add_last(3)
lnk_lst.add_last(5)
lnk_lst.add_last(7)
lnk_lst.add_last(12)
print(lnk_lst)

def insert_sorted(lnk_lst,elem):
    position = lnk_lst.first_node()
    # print(position.data)

    while elem > position.next.data:
        # print(position.data,'in')
        if position.next is not lnk_lst.trailer:
            position = position.next
            # print(position.data)
        # print(position.data,'out')
    new_node = DoublyLinkedLists.DoublyLinkedList.Node(elem)
    # print(position.data,'here')
    new_node.next = position.next
    position.next = new_node
    new_node.prev = position
    position.next.prev = new_node

    lnk_lst.size += 1

insert_sorted(lnk_lst,6)

print(lnk_lst)
print(lnk_lst.size)
