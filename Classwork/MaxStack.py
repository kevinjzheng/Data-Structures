class MaxStack:
    def __init__(self):
        self.data = []
    def push(self,x):
        currMin = self.getMin()
        self.data.append((x,min(x,currMin)))
    def pop(self):
        if self.data:
            return self.data.pop()[0]
        return None
    def top(self):
        if self.data:
            return self.data[-1][0]
        return None
    def getMin(self):
        if self.data:
            return self.data[-1][1]
        return None


print 5 > float('-inf')
# stack = MaxStack()
# stack.push(2)
# print(stack.getMax())
# stack.push(3)
# stack.push(4)
# stack.push(4)
# stack.push(6)
# print(stack.getMax())
# stack.pop()
# print(stack.getMax())
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack.getMax())
# print(stack.top())
# stack.push(6)
# print(stack.top())
