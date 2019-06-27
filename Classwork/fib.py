def fib(n):
    if (n == 1) or (n == 0) :
        return 1
    else:
        prev = fib(n-1)
        pre_prev = fib(n-2)
        return pre_prev+ prev

def fib_iter(n):
    prev = 1
    curr = 1
    for i in range(3,n+1):
        curr,prev = (prev + curr), curr
    return curr
