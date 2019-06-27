class DoublyLinkedList:
    class Node:
        def __init__(self,data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self) == 0
    def first_node(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self.header.next
    def last_node(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self.trailer.prev
    def add_first(self,new_data):
        return self.add_after(self.header,new_data)
    def add_last(self,new_data):
        return self.add_after(self.trailer.prev,new_data)
    def add_after(self,node,new_data):
        pred = node
        succ = node.next
        new_node = DoublyLinkedList.Node(new_data,succ,pred)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node
    def add_before(self,node,new_data):
        return self.add_after(node.prev,new_data)

    def add_second(self,data):
        if self.is_empty():
            raise Exception('Stack is empty')
        new_node = DoublyLinkedList.Node(data)
        new_node.next = self.header.next.next
        new_node.prev = self.header.next
        self.header.next.next.prev = new_node
        self.header.next.next = new_node
        print(self.header.next.next.data)

    def delete_node(self,node):
        pred = node.pred
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        res = node.new_data
        node.disconnect()
        return res
    def delete_first(self):
        if self.is_empty():
            raise Exception('List is emtpy')
        return self.delete_node(self.first_node)
    def delete_last(self):
        if self.is_empty():
            raise Exception('List is emtpy')
        return self.delete_node(self.last_node)
    def __iter__(self):
        if self.is_empty():
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next
    def __repr__(self):
        lst = [str(item) for item in self]
        return "[" + " <--> ".join([str(item) for item in self]) + "]"

lnk_lst2 = DoublyLinkedList()
lnk_lst2.add_first(20)
lnk_lst2.add_last(40)
print(lnk_lst2)
lnk_lst2.add_second(10)
print(lnk_lst2)
#
# lnk_lst1 = DoublyLinkedList()
# lnk_lst1.add_first(2)
# lnk_lst1.add_last(4.0)
# lnk_lst1.add_last([5,3,6])
# lnk_lst1.add_last(lnk_lst2)
#
# print(lnk_lst1)
