import DoublyLinkedLists

class BoostQueue:
    def __init__(self):
        self.data = DoublyLinkedLists.DoublyLinkedList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return self.data.is_empty()
    def enqueue(self,elem):
        self.data.add_last(elem)
    def dequeue(self):
        return self.data.delete_node(self.data.first_node())
    def first(self):
        return self.data.first_node().data
    def boost(self,k):
        position = self.data.last_node()
        for i in range(k):
            # print(position.data,position.prev.data,position.prev.prev.data)
            position.data,position.prev.data = position.prev.data,position.data
            position = position.prev


boostq = BoostQueue()
boostq.enqueue(1)
boostq.enqueue(2)
boostq.enqueue(3)
boostq.enqueue(4)
print(boostq.data)
boostq.boost(2)
print(boostq.data)
print(boostq.dequeue())
print(boostq.dequeue())
print(boostq.dequeue())
print(boostq.dequeue())
