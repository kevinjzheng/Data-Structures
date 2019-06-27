def count_lowercase(s,low,high):
    if low == high:
        if s[low].islower():
            return 1
        return 0
    else:
        rest = count_lowercase(s,low+1,high)
        if s[low].islower():
            return rest + 1
        return rest

# s = "HellO"
# print(count_lowercase(s,0,len(s)-1))

def is_number_of_lowercase_even(s,low,high):
    if low == high:
        if s[low].islower():
            return False
        return True
    else:
        rest = is_number_of_lowercase_even(s,low+1,high)
        if s[low].islower():
            return not rest
        return rest

# s = "Hello"
# print(is_number_of_lowercase_even(s,0,len(s)-1))
