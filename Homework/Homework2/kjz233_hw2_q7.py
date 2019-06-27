# def findChange(lst01):
#     for i in range(len(lst01)):
#         if lst01[i] == 1:
#             return i
#
#
# lst = [0,0,0,0,0,1,1,1]
# print(findChange(lst))
#

def findChange(lst01):
    low = 0
    high = len(lst01) - 1
    while low < high:
        mid = low + (high - low) // 2
        if lst01[mid] == 1:
            high = mid
        else:
            low = mid + 1
    return low

# lst = [0,0,0,0,0,1,1,1]
# print(findChange(lst))
