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

#Use a tuple to store the largest number and compare that number to the newly added number each time we push

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maxNum = None
    def is_empty(self):
        return self.data.is_empty()
    def __len__(self):
        return len(self.data)
    def push(self,elem):
        if self.maxNum == None:
            self.maxNum = elem
        else:
            if elem > self.maxNum:
                self.maxNum = elem
        self.data.push((elem,self.maxNum))
    def top(self):
        return self.data.top()[0]
    def pop(self):
        return self.data.pop()[0]
    def max(self):
        return self.data.top()[1]

# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(maxS.max())
# print(maxS.pop())
# print(maxS.pop())
# print(maxS.max())
