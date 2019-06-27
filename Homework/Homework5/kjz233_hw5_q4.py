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

class Queue():
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()
        self.size = 0

    def enqueue(self, val):
        self.stack1.push(val)
        self.size += 1

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise Empty("Queue is empty")
        self.size -= 1
        return self.stack2.pop()

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

# myQueue = Queue()
# myQueue.enqueue(1)
# myQueue.enqueue(2)
# myQueue.enqueue(3)
# myQueue.enqueue(4)
# print(myQueue.dequeue(), len(myQueue))
# print(myQueue.dequeue(), len(myQueue))
# print(myQueue.dequeue(), len(myQueue))
# print(myQueue.dequeue(), len(myQueue))
# print(myQueue.dequeue(), len(myQueue))
