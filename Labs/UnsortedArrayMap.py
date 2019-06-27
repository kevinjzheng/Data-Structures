class UnsortedArrayMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __getitem__(self,key):
        for item in self.table:
            if item.key == key:
                return item.value
        raise KeyError('Key Error: '+ str(key))
        
    def __setitem__(self,key,value):
        for item in self.table:
            if item.key == key:
                item.value = value
        new_item = UnsortedArrayMap.Item(key,value)

    def __delitem__(self,key):
        for i in range(len(self)):
            if self.table[i].key == key:
                self.table.pop[i]
                return
        raise KeyError('Key Error: '+ str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key
