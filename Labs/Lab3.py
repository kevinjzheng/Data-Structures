#Problem 1
def reverse_vowels(input_string):
    i = 0
    n = len(input_string)
    j = n-1
    lst1 = [""] * n
    #print(n)
    for x in range(n):
        lst1[x] = input_string[x]
    #print(lst1)
    vowel = "aeiou"
    #print(i,j)
    preventcrash = 0;
    while ((i <= j) and preventcrash<100):
        #print(i,j)
        preventcrash +=1
        #print(lst1[i], lst1[j])
        if lst1[i] in vowel and lst1[j] in vowel:
            lst1[i],lst1[j] = lst1[j],lst1[i]
            i += 1
            j -= 1
        if lst1[i] == "a" or lst1[i] == "e" or lst1[i] == "i" or lst1[i] == "o" or lst1[i] == "u":
            j -= 1
        elif lst1[j] == "a" or lst1[j] == "e" or lst1[j] == "i" or lst1[j] == "o" or lst1[j] == "u":
            i += 1
        else:
            i+=1
            j-=1
    #print(i,j)
    newString = "".join(lst1)
    return(newString)
test = reverse_vowels("tandon")
test = reverse_vowels("schoolbus")
print(test)

#Problem 2
lst11 = [1,6,14,15]
lst12 = [2,6,14,19]



# Problem 3
def sqrt(num):
    x = 0
    while (x * x) < num:
        x += 0.01
    return x

print(sqrt(100))

def square_root(n):
    lo = 0
    hi = n
    mid = (lo+hi) / 2

    while abs((mid * mid) - n) > 0.001:
        if mid * mid > n:
            lo = mid
        else:
            hi = mid
        mid = (lo + hi) / 2
    return mid

print(square_root(100))
