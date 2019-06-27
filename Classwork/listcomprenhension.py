class Counter:
    def __init__(self):
        self.value = 0
    def inc(self):
        self.value += 1
    def __repr__(self):
        return str(self.value)

c1 = Counter()
print(c1.value)
c1.inc()
print(c1.value)
c1.inc()
print(c1.value)
c1.inc()
print(c1)
print("-------")
A = [Counter()] * 3
for c in A:
    c.inc()
    print(c)

B = [Counter() for i in range(3)]
for c in B:
    c.inc()
    print(c)
print('-------')
lst = [1,2,3]
s = "abc"
r = range(3)
lst_iter = iter(lst)
print(lst_iter)
s_iter = iter(s)
print(type(s_iter))
r_iter = iter(r)
print(type(r_iter))
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
#   print(next(lst_iter)) # it returns a "Stop Iteration" and an error message
print("-------")

for curr in s:
    print(curr)

print('--or--')

s = "abc"
s_iter1 = iter(s)
s_iter2 = iter(s)
# you can create as many iterators as you want and iterate each one at its own pace
end = False
while(end == False):
    try:
        curr = next(s_iter1)
        print(curr)
    except StopIteration:
        end = True
print('-------')

# for elem in range(3,10,0.5):
#     print(elem)

def my_range_list(start,end,step):
    curr = start
    res = []
    while curr < end:
        res.append(curr)
        curr += step
    return(res)

for elem in my_range_list(3,10,0.5):
    print(elem)

print('------')
