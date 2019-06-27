#Vitamins
class ArrayQueue:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = item
        self.number_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0

q = ArrayQueue()
i = 2
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(8)
i += q.first()
q.enqueue(i)
q.dequeue()
q.dequeue()
# print(i)
# print(q.first())


#dequeue Question 1
class ArrayDeQueue:
    intial_capacity = 5
    def __init__(self):
        self.data = [None] * ArrayDeQueue.intial_capacity
        self.front_ind = 0
        self.num_of_elems = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        if len(self) == 0:
            return True
        return False
    def add_last(self,item):
        if self.num_of_elems == len(self.data):
            self.resize(len(self.data)*2)
        end_ind = (self.front_ind + self.num_of_elems) % len(self.data) # this creates a looping effect when there isn't enough space
        self.data[end_ind] = item
        self.num_of_elems += 1
    def delete_first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.num_of_elems < (len(self.data) // 4):
            self.resize(len(self.data)//2)
        return value
    def add_first(self,item):
        if self.num_of_elems == len(self.data):
            self.resize(len(self.data)*2)
        self.front_ind = (self.front_ind - 1) % len(self.data)
        self.data[self.front_ind] = item
        self.num_of_elems += 1
    def delete_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        back_ind = (self.front_ind + len(self) - 1) % len(self.data)
        value = self.data[back_ind]
        self.data[back_ind] = None
        back_ind = (back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if self.num_of_elems < (len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]
    def last(self):
        back_ind = (self.front_ind + len(self) - 1) % len(self.data)
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[back_ind]
    def resize(self,new_size):
        old_data = self.data
        self.data = [None] * new_size
        old_ind = self.front_ind
        for new_ind in range(new_size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

q = ArrayDeQueue()
q.add_last(21)
q.add_last(22)
q.add_first(1)
q.add_first(2)
q.add_first(3)
# q.add_last(23)
#q.add_last(4)
print(q.front_ind)
print(q.data)
print(len(q))
print(q.last())
print(q.first())
q.delete_last()
print(q.data)
q.delete_first()
print(q.data)
print(q.first())
print(q.last())

#Question 2
class Boost:
    def boost(self,k):
        q = self.Queue
        d = q.data
        k = min(k,len(q)-1)
        back = (q.front_ind + len(q) - 1) % len(d)
        for elem in range(k):
            before = (back - 1) % len(d)
            d[back],d[before] = d[before],d[back]
            back = before
