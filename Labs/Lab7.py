# def get_tag():

class ArrayStack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        if len(self) == 0:
            return True
        return False
    def push(self,elem):
        self.data.append(elem)
    def pop(self):
        if self.is_empty() == True:
            raise Exception("Stack is empty")
        return self.data.pop()
    def top(self):
        if self.is_empty() == True:
            raise Exception("Stack is empty")
        return self.data[-1]


def infix_to_prefix(expr):
    ops = ArrayStack()
    arg = ArrayStack()
    result = ""
    for elem in expr.split():
        # print(elem)
        if elem.isdigit():
            arg.push(elem)
        elif elem in "+-/*()":
            ops.push(elem)
    print(ops.data)
    print(arg.data)
    while not ops.is_empty():
        break


print(infix_to_prefix('( 23 + 2 ) * 2'))

#   * 2 + 2 23
#
# def eval_postfix_boolen_exp(boolean_exp_str):
#     edit = boolean_exp_str.split(" ")
#     print(edit)
#     j = []
#     for i in range(len(boolean_exp_str)): #loop for checking each characer one by one
#         if(boolean_exp_str[i].isdigit()==True): #if the character is a digit that will be stored in another array j
#             j.append(int(boolean_exp_str[i]))
#         elif(boolean_exp_str[i]=='*'):
#     #if * operator then first pop will pop the last element and second pop will do the last-1 element.
#     #now we need to swap as the left most between the two will be operand 1, and operand2 will be the right one.
#         	x=j.pop()
#         	y=j.pop()
#         	res = y * x
#         	j.append(res)
#         elif(boolean_exp_str[i]=='+'):
#         	x=j.pop()
#         	y=j.pop()
#         	res = y + x
#         	j.append(res)
#         elif(boolean_exp_str[i]=='-'):
#     #if * operator then first pop will pop the last element and second pop will do the last-1 element.
#     #now we need to swap as the left most between the two will be operand 1, and operand2 will be the right one.
#     #ex: if 6,4 is appended and we do operation withour swapping it'll be 4-6=-2
#         	x=j.pop()
#         	y=j.pop()
#         	res = y - x
#         	j.append(res)
#         elif(boolean_exp_str[i]=='/'):
#     #ex: if we do not swap 6,3 will be resulted as 3/6.
#         	x=j.pop()
#         	y=j.pop()
#         	res=y/x
#         	j.append(res)
#         elif(boolean_exp_str[i]=='<'):
#             x = j.pop()
#             y = j.pop()
#             if x > y:
#                 res = True
#             else:
#                 res = False
#             j.append(res)
#     print('Your postfix expression result is',j[0])
#
# eval_postfix_boolen_exp('2 5 <')
# eval_postfix_boolen_exp('2 3 4 * 5 - +')
