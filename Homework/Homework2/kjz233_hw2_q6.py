def two_sum(srt_lst,target):
    output = None
    for i in range(len(srt_lst)):
        difference = target - srt_lst[i]
        if srt_lst.count((difference)) == 1:
            output = (i,srt_lst.index(difference))
            return output
    return output


# lst = [-2,7,11,15,20,21]
# num = 22
# num = 18
# num = 26
# # num = 3
# print(two_sum(lst,num))
