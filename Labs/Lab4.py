import ctypes

def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)   #makes the array
        self.n = 0  #intial number of elements in the array
        self.capacity = 1   #intial max capacity for how many elements the array can store
    def append(self,val):
        if(self.n == self.capacity):    #this check if there is enough space, if not then it will make a larger array first
            self.resize(2*self.capacity)
        self.data[self.n] = val     #add its to the next space if there is enough space
        self.n += 1
    def resize(self,new_size):
        new_arr = make_array(new_size)   #new array will be twice the length of the previous array
        for i in range(self.n):
            new_arr[i] = self.data[i]   #copying over the values from the existing array
        self.data = new_arr     #reassigning the data to be the new array
        self.capacity = new_size     #new capacity is now twice as long as it was before
    def __len__(self):
        return self.n
    def __getitem__(self,index):
        if not((-1*self.n) <= index <= (self.n - 1)):
            raise IndexError("invalid index")   #returns an error message if error
        if index < 0:
            return self.data[self.n + index]
        else:
            return self.data[index]
    def __setitem__(self,index,new_val):
        if not((-1*self.n) <= index <= (self.n - 1)):
            raise IndexError("invalid index")   #returns an error message if error
        if index < 0:
            self.data[self.n + index] = new_val
        else:
            self.data[index] = new_val
    def iter(self):
        for i in range(self.n):
            yield self.data[i]
    def extend(self,iterable_collection):
        for element in iterable_collection:
            self.append(element)
    def insert(self,index,val):
        if (index > self.capacity) or (index < (self.capacity * -1)):
            pass
    def __add__(self,other):
        lstNew = MyList()
        lstNew.extend(self)
        lstNew.extend(other)
        return lstNew
    def __iadd__(self,other):
        self.extend(other)
        return self
    def __repr__(self):
        return "["+", ".join([str(x) for x in self])+"]"
    def __mul__(self,num):
        lstNew = MyList()
        for i in range(num):
            lstNew.extend(self)
        return lstNew
    def __rmul__(self,num):
        lstNew = MyList()
        for i in range(num):
            lstNew.extend(self)
        return lstNew

lst = MyList()
for i in range(5):
    lst.append(i)
print(lst)
lst.extend([1,2,3])
print(lst)
lst1 = MyList()
lst2 = MyList()
for j in range(5):
    lst1.append(j)
for k in range(6,10):
    lst2.append(k)
print(lst1)
print(lst2)

lst4 = lst1 + lst2
print(lst4)
lst2 += lst1
print(lst2)
print(lst2[-9])
print(lst2[-1])
print(lst1)
print(lst1 * 3)
print(2 * lst1)
print(lst1)
lst1[-1] = 3
print(lst1)
