import math
def factors(num):
    for i in range(1,int(math.sqrt(num)+1)):    #n^(1/2)
        if num % i == 0:
            yield i

    for i in range(int(math.sqrt(num)+1),0,-1):
        if num % (num // i) == 0 and (num // i) != math.sqrt(num):
            yield (num // i)


# for curr_factor in factors(1000000000000):
#     print(curr_factor)
