#Problem 1
import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()
    def push(self,e):
        ''' Add element e to the top of the stack '''
        self.data.add_last(e)
    def pop(self):
        ''' Remove and return the top element from the stack. If the
        stack is empty, raise an exception'''
        return self.data.delete_node(self.data.last_node())
    def top(self):
        ''' Return a reference to the top element of the stack without
        removing it. If the stack is empty, raise an exception '''
        return self.data.last_node().data
    def is_empty(self):
        ''' Return True if stack is empty'''
        return self.data.is_empty()
    def __len__(self):
        '''Return the number of elements in the stack'''
        return len(self.data)

# link = LinkedStack()
# link.push(2)
# print(link.top())
# print(link.pop())
# print(link.is_empty())
# print(len(link))
# link.push(1)
# link.push(2)
# link.push(3)
# print(len(link))

#Problem 2
class LeakyStack:
    def __init__(self,max_num_of_elems):
        self.data = DoublyLinkedList.DoublyLinkedList()
        '''An empty leaky stack implemented using a doubly linked
        list'''
        self.size = 0
        self.max_elems = max_num_of_elems
    def push(self,e):
        '''Add element e to the top of the stack'''
        if self.size == self.max_elems:
            self.data.delete_node(self.data.first_node())
        self.data.add_last(e)
        self.size += 1
    def pop(self):
        '''Remove and return the top element from the stack. If the
        stack is empty, raise an exception'''
        return self.data.delete_node(self.data.last_node())
    def top(self):
        '''Return a reference to the top element of the stack without
        removing it. If the stack is empty, raise an exception'''
        return self.data.last_node()
    def is_empty(self):
        '''Return True if stack is empty'''
        return self.data.is_empty()
    def __len__(self):
        '''Return the number of elements in the stack'''
        return self.data.size

# leaky = LeakyStack(5)
# leaky.push(1)
# leaky.push(2)
# leaky.push(3)
# leaky.push(4)
# leaky.push(5)
# print(leaky.data)
# leaky.push(6)
# print(leaky.data)

#Problem 3
'''Return the sum of the values in the linked list'''
linked = DoublyLinkedList.DoublyLinkedList()

# Method 1
def sum_lnk_lst(lnk_lst):
    return helper(lnk_lst.first_node())

def helper(curnode):
    if curnode.next is None:
        return 0
    return curnode.data + helper(curnode.next)

# Method 2
# def sum_lnk_lst(lnk_lst):
#     return helper(lnk_lst, lnk_lst.first_node())
#
# def helper(lnk_lst, curnode):
#     if curnode is lnk_lst.trailer:
#         return 0
#     return curnode.data + helper(lnk_lst, curnode.next)

linked.add_first(2)
linked.add_first(4)
linked.add_first(6)
linked.add_first(8)

print(linked)
# print(linked.header.next.data)
# # print(sum_lnk_lst(linked))
# print(linked.first_node().data)

#Problem 4
# def reverse_list_change_elements_order(lnk_lst):
#     '''Reverses the linked list'''
#     flipper(lnk_lst.header,lnk_lst.trailer)
# def flipper(curnode):
#     # print(curnode.data)
#     if curnode.next.data is None:
#         return
#     curnode.data,curnode.next.data = curnode.next.data,curnode.data
#     flipper(curnode.next)

# def flipper(front,back):
#     if front == back:
#         return
#     front.data,back.data = back.data,front.data
#     flipper(front.next,back.prev)
#
# reverse_list_change_elements_order(linked)
# print(linked)

def reverse(lst):   #two cursors, swaps elements    works for singly and doubly
    i = lst.first_node()
    j = lst.last_node()
    while i is not j and i.prev is not j: #this accounts for the even number of elems too
        i.data,j.data = j.data,i.data
        i = i.next
        j = j.prev

reverse(linked)
print(linked)

def rev(lst):   #one cursor, swaps order    this is how you reverse for singly linked list
    i = lst.header
    while i is not None:
        i.prev,i.next = i.next,i.prev
        i = i.prev
    lst.header,lst.trailer = lst.trailer,lst.header
def reverse_list_change_nodes_order(lnk_lst):
    '''Reverses the linked list'''
    i = lnk_lst.header
    while i is not None:
        i.prev,i.next = i.next,i.prev
        i = i.prev
    lnk_lst.header,lnk_lst.trailer = lnk_lst.trailer,lnk_lst.header

reverse_list_change_nodes_order(linked)
