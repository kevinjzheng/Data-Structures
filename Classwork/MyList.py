import ctypes # provides low-level arrays

def make_array(n):
    return (n * ctypes.py_object)()

# arr = make_array(15)
# arr[0] = 7
# arr[3] = 5

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
        if not(0 <= index <= (self.n - 1)):
            raise IndexError("invalid index")   #returns an error message if error
        return self.data[index]
    def __setitem__(self,index,new_val):
        if not(0 <= index <= (self.n - 1)):
            raise IndexError("invalid index")   #returns an error message if error
        self.data[index] = new_val
        return self.data[index]
    def iter(self):
        for i in range(self.n):
            yield self.data[i]
    def extend(self,iterable_collection):
        for element in iterable_collection:
            self.append(element)
    def __add__(self):
        pass

    def __repr__(self):
        pass

lst = MyList()
for i in range(5):
    lst.append(i)
# print(len(lst))
# lst.append(10)
# lst.append(20)
# lst.append(30)
# lst.append(40)
# lst.append(50)
# print(len(lst))
# print(lst.capacity)
# print(lst.data[2])
# print(lst[2])   # __getitem__ overload allows this to work
# lst[2] = 40
# print(lst[2])
for i in lst:
    print i
