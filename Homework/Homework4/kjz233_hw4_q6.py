
def appearances(s,low,high):
    if low == high:
        return {s[low]:1}
        # d{s[low]} = 1
    else:
        rest = appearances(s,low+1,high)
        if s[low] in rest:
            # d{low} += 1
            rest[s[low]] += 1
        else:
            # d{low} = 1
            rest[s[low]] = 1
        return rest

# s = "Hello World"
# # s = "HH"
# print(apperances(s,0,len(s)-1))
