#Problem 1
def powers_of_two(num):
    for i in range(1,num+1):
        yield 2**i

for curr_value in powers_of_two(6):
    print(curr_value)

#Problem 2
def nested_sum(lst):
    total = 0
    for elem in lst:
        if isinstance(elem,list):
            total = nested_sum(elem)
        else:
            total += elem
    return total
lst = [[1,2],[3,[[4],5]],6]
print(nested_sum(lst))

#Problem 3
def sort_first(lst):
    #pivotNum = lst[0]
    pivot = 0
    i = 1
    while i < len(lst):
        if lst[i] < lst[pivot]:
            lst[pivot],lst[i] = lst[i],lst[pivot]
            pivot += 1
            lst[pivot],lst[i] = lst[i],lst[pivot]
            # lst[pivot] = lst[i]
            # pivot += 1
            # lst[i] = lst[pivot]
            # lst[pivot] = pivotNumx`x`
        i += 1

    return lst
lst = [54,26,93,94,95,17,77,31,44,55,20]
print(sort_first(lst))

#Problem 4
