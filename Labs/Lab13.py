import random
import UnsortedArrayMap

class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnsortedArrayMap.UnsortedArrayMap()
        old_size = len(self.table[i])
        self.table[i][key] = value
        new_size = len(self.table[i])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[i] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value

def most_frequent(lst):
    bank = {}
    for item in lst:
        if item in bank:
            bank[item] += 1
        else:
            bank[item] = 1
    return max(bank.keys())

lst = [5,9,2,9,0,5,9,7]
print(most_frequent(lst))

class OpenAddressingMap:
    class Item:
        def __init__(self,key,value=None):
            self.key = key
            self.value = value
    class DeletedItem:
        pass
    def __init__(self,N=10):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.marker = DeletedItem()

    def __len__(self):
        return self.n
    def is_empty(self):
        return self.n == 0
    def __getitem__(self,key,value):
        i = hash(key) % self.N
        while self.table[i] is not None:
            if not self.table[i] is self.marker and self.table[i].key == key:
                return self.table[i].value
            i = (i+1) % self.N
        else:
            raise KeyError('Key Error:' + str(key))
    def __setitem__(self,key,value):
        hashed_key = hash(key) % self.N
        first_del = None
        while self.table[i] is not None:
            if self.table[i] is self.marker and first_del is None:
                first_del = i
            elif self.table[i].key == key:
                self.table[i].value = value
                return
                i = (i+1) % self.N
        if first_del is not None:
            self.table[first_del] = self.Item(key,value)
        else:
            self.table[i] = self.Item(key,value)
        self.m += 1
        if self.n > .5 * self.N:
            self.hash(2*self.N)

    def __delitem__(self):
        pass
    def __iter__(self):
        pass
    def rehash(self):
        pass
