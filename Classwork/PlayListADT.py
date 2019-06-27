import UnsortedArrayMap
import random

class ChainingHashTableMap:
    def __init__(self,N = 64,p = 40206835204840513073):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randint(1,self.p - 1)
        self.b = random.randint(0,self.p - 1)
    def __len__(self):
        return self.n

    def hash_function(self,key):
        return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __getitem__(self,key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError('Key Error:' + str(key))
        return curr_bucket[key]

    def __setitem__(self,key,value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnsortedArrayMap.UnsortedArrayMap()
        old_size = len(self.table[i])
        (self.table[i])[key] = value
        new_size = len(self.table[i])
        if new_size > old_size:
            self.n += 1
        if self.n > self.N:
            self.rehash(2 * self.N)

    def __delitem__(self,key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError('Key Error:' + str(key))
        del curr_bucket[key]
        self.n -= 1
        if curr_bucket.is_empty():
            self.table[i] = None
        if self.n < self.N//4:
            self.rehash(N//2)

    def __iter__(self):
        pass
    def rehash(self):
        old_data = []
        for key in self:
            old_data.append((key,self[key]))
        self.table = [None] * new_size
        self.N = new_size
        self.n = 0
        for (key,val) in old_data:
            self[key] = val

class Playlist:
    def __init__(self):
        self.data = ChainingHashTableMap()
    def add_song(self,new_song_name):
        self.data.add_last(new_song_name)
    def add_song_after(self,song_name,new_song_name):
        self.data.add_after(song_name,new_song_name)
    def play_song(self,song_name):
        pass
    def play_list(self):
        pass
