import ArrayStack

class DupStack:
    def __init__(self):
        self.data = ArrayStack.ArrayStack()
        self.dup = 1
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return self.data.is_empty()
    def pop(self):
        if self.data.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()
    def top(self):
        if self.data.is_empty():
            raise Exception('Stack is empty')
        return self.data.top()
    def push(self,elem):
        self.data.push(elem)
    def pop_dups(self):
        # popped = ArrayStack.ArrayStack()
        # popped.push(self.data.top())
        # while self.data.top() == popped.top():
        #     popped.push(self.data.pop())
        # return popped.top()
        if self.data.is_empty():
            raise Exception('Stack is Empty')
        self.dup = self.data.top()
        while self.data.top() == self.dup:
            self.data.pop()
        return self.dup
    def top_dups_count(self):
        # count = ArrayStack.ArrayStack()
        # count.push(self.data.pop())
        # while self.data.top() == count.top():
        #     count.push(self.data.pop())
        # for i in range(len(count)):
        #     self.data.push(count.top())
        # return len(count)
        if self.data.is_empty():
            raise Exception('Stack is Empty')
        self.dup = self.data.top()
        count = 0
        while self.data.top() == self.dup:
            self.data.pop()
            count += 1
        for i in range(count):
            self.data.push(self.dup)
        return count
        
dupS = DupStack()
dupS.push(4)
dupS.push(5)
dupS.push(5)
dupS.push(5)
dupS.push(4)
dupS.push(4)
print(dupS.data.data)
print(dupS.pop_dups())
print(dupS.data.data)
print(dupS.pop_dups())
print(dupS.data.data)
# print(len(dupS))
# print(dupS.top())
# print(dupS.top_dups_count())
# # print(dupS.data.data)
# print(dupS.pop())
# print(dupS.pop())
# print(dupS.top())
# print(dupS.top_dups_count())
# print(dupS.pop_dups())
# print(dupS.top())
