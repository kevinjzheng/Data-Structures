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

variables = {}
def post_fix_calculator(userInput):
    plates = userInput.split() # takes care of the number of spaces in between each element
    stack = ArrayStack()
    ans = ""
    # print(plates)
    for plate in plates:
        # print(plate)
        if plate in variables:
            # print('true')
            stack.push(variables[plate])
        elif plate.isdigit():
            stack.push(int(plate))
        elif plate == "=":
            ans = stack.pop()
            # print(ans)
        elif plate == "+":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 + arg2)
        elif plate == "-":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 - arg2)
        elif plate == "*":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 * arg2)
        elif plate == "/":
            arg2 = stack.pop()
            arg1 = stack.pop()
            if arg2 == 0:
                raise ZeroDivisionError('division by zero')
            stack.push(arg1 / arg2)
        else:
            stack.push(plate)
    if ans == "":
        return stack.pop()
    else:
        variables[ans] = stack.pop()
        # print(variables)
        return ans

def main():
    done = False
    while done == False:
        userInput = input("-->")
        if userInput != "done()":
            print(post_fix_calculator(userInput))
        else:
            done = True

main()
