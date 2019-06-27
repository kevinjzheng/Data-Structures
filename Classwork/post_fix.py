import ArrayStack

def eval_postfix_exp(exp_str):
    args_stack = ArrayStack.ArrayStack()

    for token in exp_str.split():
        if token not in "+-*/":
            args_stack.push(int(token))
        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if token == '+':
                res = arg1+arg2
            elif token == '-':
                res = arg1-arg2
            elif token == '*':
                res = arg1*arg2
            elif token == '/':
                if arg2 == 0:
                    raise ZeroDivisionError('division by zero')
                res = arg1/arg2
            args_stack.push(res)
    return args_stack.pop()

def eval_infix_exp(exp_str):
    args_stack = ArrayStack.ArrayStack()
    ops_stack = ArrayStack.ArrayStack()

    for token in tokens(exp_str):
        if token.isdigit(): # token is a number
            args_stack.push(int(token))
        elif token == "(":
            ops_stack.push(token)
        elif token in "+-*/":
            ops_stack.push(token)
        else:   #token == ")"
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            op = ops_stack.pop()
            ops_stack.pop() # the extra "("
            if op == '+':
                res = arg1+arg2
            elif op == '-':
                res = arg1-arg2
            elif op == '*':
                res = arg1*arg2
            elif op == '/':
                if arg2 == 0:
                    raise ZeroDivisionError('division by zero')
                res = arg1/arg2
            args_stack.push(res)
    return args_stack.pop() # your result which should be the last argument in the args_stack

def tokens(exp_str):
    exp_str = exp_str.strip()   #removes the whitespace from the string from the front and back of the string
    n = len(exp_str)
    i = 0
    while(i < n):
        #skipping spaces
        while exp_str[i] == " ":
            i += 1
        if exp_str[i] in "()+-*/":
            yield exp_str[i]
            i += 1
        else:
            digits_list = []
            while (i < n) and (exp_str[i].isdigit()):
                digits_list.append(exp_str[i])
                i += 1
            yield ''.join(digits_list)
infix_exp = "(21   *( (  314 + 4 ) - 5      )) "
# print(list(tokens(infix_exp)))
print(eval_infix_exp(infix_exp))
