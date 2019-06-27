# s ="abc"
# def func(s):
#     s = s.upper()
#     print('inside',s)
# func(s)
# print(s)

# import copy
# lst = [1, 2, 3, 4]
# lst_copy = copy.copy(lst)
# lst_copy[0] = 10
# lst_copy[2] = 30
#
# print(lst)
# print(lst_copy)


#print([b * b // 2 +5 for b in range(4) if b % 3 == 0])
#print([2**i for i in range(9)])
#print([i**3 for i in range(6)])
#print([curr for curr in range(1,43) if (42%curr) == 0])

# Problem 1
class Polynomial:
    def __init__(self,lst = [0]):
        self.lst = lst
    def eval(self,val):
        rev = self.lst[::-1]
        #print(self.lst)
        ans = 0
        power = len(rev)
        for i in range(len(rev)):
            ans += (rev[i]*(val**(power-(i+1))))
            #print(ans)
        return ans
    def __add__(self,rhs): # we are taking an object and not a list
        lst3 = []
        if len(self.lst) < len(rhs.lst):
            shorterLen = len(self.lst)
            longerLen = len(rhs.lst)
            shorter = self.lst
            longer = rhs.lst
        else:
            shorterLen = len(rhs.lst)
            longerLen = len(self.lst)
            shorter = rhs.lst
            longer = self.lst
        #print(longerLen)
        # loop through both and if the shorter list is done then just copy from the longer list if not then add from the shorter list
        for i in range(longerLen):
            if i < shorterLen:
                lst3.append(shorter[i]+longer[i])
                #print(lst3)
            elif i >= shorterLen:
                lst3.append(longer[i])
                #print(lst3)
        return Polynomial(lst3)
    def __mul__(self,rhs):
        lst3 = [0] * ((len(self.lst)-1) * (len(rhs.lst)-1))

        for i in range(len(rhs.lst)):
            for j in range(len(self.lst)):
                lst3[i+j] += (self.lst[j] * rhs.lst[i])

        return Polynomial(lst3)
    def __repr__(self):
        string = ""
        for i in range(len(self.lst)-1,0,-1):
            if self.lst[i] != 0:
                if self.lst[i-1] < 0:
                    oper = "-"
                else:
                    oper = "+"
                string += str(abs(self.lst[i])) + "x^" + str(i) + oper

        string += str(self.lst[0])
        return string

polynomial = Polynomial([3,7,0,-9,2])
polyB = Polynomial([0,9,0,0,0,0,0,0,0,3])
print(polynomial.eval(2))
# overload the addition operator allowing you to add objects directly
print(polynomial + polyB)
print(polynomial * polyB)

# Problem 2
L = [2,3,5,6,8,8]
# print([L[i] for i in range(len(L)) if i % 2 == 0 and L[i] % 2 == 0]) #CORRECT

# --------------------------------------------------------------------------------------
#Addition
# lst1 = [3,7,1,-9,2]
# lst2 = [0,9,0,0,0,0,0,0,0,3]
# count = 0
# lst3 = []
# if len(lst1) < len(lst2):
#     shorter = len(lst1)
#     longer = len(lst2)
# else:
#     shorter = len(lst2)
#     longer = len(lst1)
# print(longer)
# # loop through both and if the shorter list is done then just copy from the longer list if not then add from the shorter list
# for i in range(longer):
#     if i < shorter:
#         lst3.append(lst1[i]+lst2[i])
#         print(lst3)
#     elif i >= shorter:
#         lst3.append(lst2[i])
#         print(lst3)

# Multiplication
# lst1 = [1,2,3]
# lst2 = [2,0,6,8]
# lst3 = [0] * ((len(lst1)-1) * (len(lst2)-1))
#print(lst3)
#
# for i in range(len(lst2)):
#     for j in range(len(lst1)):
#         lst3[i+j] += (lst1[j] * lst2[i])

#print(lst3)

# string = ""
# for i in range(len(lst)-1,0,-1):
#     if lst[i] != 0:
#         if lst[i-1] < 0:
#             oper = "-"
#         else:
#             oper = "+"
#         string += str(abs(lst[i])) + "x^" + str(i) + oper
#
# string += str(lst[0])
# print(string)
