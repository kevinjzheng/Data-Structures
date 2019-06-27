def count_down(start,end):  #assume that when calling count_down on a smaller range it would print the
                            #numbers of that range in a decreasing order
    if (start == end):
        print(start)
    else:
        count_down(start+1,end) #this is print the entire range in decreasing order from end to
                                #start+1
        print(start)

def count_up_and_down(start,end):
    if (start == end):
        print(start)
    else:
        print(start)
        count_up_and_down(start+1,end)
        # print(start)
        print(start)
# count_up_and_down(1,5)


# assume when calling factorial with a k(< n) it would return the k!
def factorial(n):
    if n == 1:
        return 1
    else:
        result = factorial(n-1)
        return n * result

# print(factorial(5))

# assume when calling count_appear on a smalelr list it would return the count the number of appearances of val in the list
def count_appear(lst,val):
    if len(lst) == 0:
        return 0
    else:
        occurances = count_appear(lst[1:],val)
        if lst[0] == val:   #checks the first value in the shrinker list
            return occurances + 1
        else:
            return occurances

# print(count_appear([2,4,3,5,3,2,1,1],2))

def count_appear_linear(lst,low,high,val):
    if low == high:           
        if lst[low] == val:
            return 1
        else:
            return 0
    else:
        count = count_appear_linear(lst,low+1,high,val)
        if lst[low] == val:
            return count + 1
        else:
            return count

def count_appear_easy(lst,val):     #count_appear_easy isnt the recursive but the count_appear_linear is the recursive function
                                    #the recursive function has to call itself
    if len(lst) == 0:
        return 0
    else:
        return count_appear_linear(lst,0,len(lst),val)

# count_appear_easy([],2)
