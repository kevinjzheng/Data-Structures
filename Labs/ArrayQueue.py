class ArrayQueue:
    intial_capacity = 5
    def __init__(self):
        self.data = [None] * ArrayQueue.intial_capacity
        self.front_ind = 0
        self.num_of_elems = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        if len(self) == 0:
            return True
        return False
    def enqueue(self,item):
        if self.num_of_elems == len(self.data):
            self.resize(len(self.data)*2)
        end_ind = (self.front_ind + self.num_of_elems) % len(self.data) # this creates a looping effect when there isn't enough space
        self.data[end_ind] = item
        self.num_of_elems += 1
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        valye = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.num_of_elems < (len(self.data) // 4):
            self.resize(len(self.data)//2)
        return value
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]
    def resize(self,new_size):
        old_data = self.data
        self.data = [None] * new_size
        for new_ind in range(new_size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
