# # Vitamins 3a
# def factorial(num):
#     value = 1
#     for i in range(1,num+1):
#         value *= i
#         yield value
# for val in factorial(5):
#     print(val)
# # Vitamins 3b
# def letters(word):
#     for i in range(len(word)):
#         yield word[i]
# for l in letters('computer'):
#     print(l)

# Coding 1a
import random
def roll_the_dice_str(n):
    s = ""
    for i in range(1,n+1):
        curr_val = random.randint(1,6)
        s = s + str(curr_val) + " " # the length of s change each iteration and thus this is not a linear function  => (n^2)
    return s[:-1]
# when n is a really large number but it will still be a constant
print(roll_the_dice_str(10))
# Coding 1b
def roll_the_dice_str_linear(n):
    lst = [" "] * n
    for i in range(1,n+1):
        curr_val = str(random.randint(1,6))
        lst[i-1] = str(int(curr_val))
    result = " ".join(lst)
    return result
print(roll_the_dice_str_linear(10))

# Coding 2
# the objective was to take the three given functions in maxSubsequenceSum
# and you test the run times and put the data into csv file and you open it in excel
# and you find how the run time correlates with the graph (linear,qudratic,cubic,exponential,.....)

# Coding 3
def move_zeroes(lst):
    write_ind = 0
    for read_ind in range(len(lst)):
        if(lst[read_ind] != 0):
            lst[write_ind] = lst[read_ind]
            write_ind += 1
    for write_ind in range(write_ind, len(lst)):
        lst[write_ind] = 0

lst = [0,1,0,3,13]
(move_zeroes(lst))
print(lst)
