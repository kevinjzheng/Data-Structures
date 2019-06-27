class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()


class Empty(Exception):
    pass

class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()
    front = 0
    for i in range(len(lst)):
        lst[i],lst[front] = lst[front],lst[i]
        for elem in lst:
            stack.push(elem)
        for num_of_remaining_elems in range(1,len(lst)-1):
            for j in range(num_of_remaining_elems + 1,len(lst)):
                lst[j],lst[num_of_remaining_elems] = lst[num_of_remaining_elems],lst[j]
                for elem in lst:
                    stack.push(elem)
                lst[num_of_remaining_elems],lst[j] = lst[j],lst[num_of_remaining_elems]
        lst[i],lst[front] = lst[front],lst[i]
    while stack.is_empty() == False:
        res = []
        for i in range(len(lst)):   #this pops as many elems there are in the list, thus creating the permutations
            res.append((stack.pop()))
        res = res[::-1]
        queue.enqueue(res)  #once the permutations are created you queue the permutation to the queue and return the queue
    res = []
    while queue.is_empty() == False:
        res.append(queue.dequeue())
    return res

lst = [1,2,3]
result = permutations(lst)
for i in range(len(result)):
    print(result[i])
