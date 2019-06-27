def f():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

print(type(f))
collection = f()
print(type(collection))
collection_iter = iter(collection)
print(type(collection_iter))
print(next(collection_iter))
print(next(collection_iter))
print(next(collection_iter))
#print(next(collection_iter))

def my_range(start,end,step):
    curr = start
    res = []
    while curr < end:
        yield curr # yield makes it only when next is called and isnt making the whole instance at one time.
        curr += step

for elem in my_range(3,10,0.5):
    print(elem)

#when iter and the collection is called, there is no memory or time consumed for this action
#only when next is called is time and memory used (the generator)
#a collection can be made to be infinite but as long as the call to next isn't infinite, the call won't
# cause it to continue evaluating.

def is_prime1(num):
    count = 0
    for curr in range(1,num+1):
        if num % curr == 0:
            count += 1
        if (count == 2):
            return True
        else:
            return False


def is_prime2(num):
    count = 0 # 1 (1)
    for curr in range(1,(num/2)+1): # range and iter (2)
        if num % curr == 0: # (5)
            count += 1
            if(count == 1): # there will only be one because the last will be num and num is its own divisor.
                return True
            else:
                return False

import math
def is_prime3(num):
    count = 0
    for curr in range(1,math.sqrt(num)+1):
        if num % curr == 0:
            count += 1
        if (count == 1):
            return True
        else:
            return False
