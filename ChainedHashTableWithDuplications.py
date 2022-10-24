from Interfaces import Set
from DLList import DLList
import ChainedHashTable 

class ChainedHashTableWithDuplications(Set):
    def __init__(self) :
        self.chainHashTable = ChainedHashTable.ChainedHashTable()
        self.n = 0

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        l = self.chainHashTable.t[self.chainHashTable.hash(key)]
        list = DLList()
        for i in range(len(l)):
            if l[i].key == key:
                list.append(l[i].value)
        return list
    
    def add(self, key : object, value : object) :
        if key<0:
            raise IndexError
        if self.n==len(self.chainHashTable.t):
            self.chainHashTable.resize()
        self.chainHashTable.t[self.chainHashTable.hash(key)].append(self.chainHashTable.Node(key,value))
        self.n+=1
        return True

    def remove(self, key : int)  -> object:
        if key<0 or self.n==0 or self.find(key)==None:
            raise IndexError()
        c = self.chainHashTable.t[self.chainHashTable.hash(key)]
        for i in range(len(c)):
            if c[i].key == key:
                c.remove(i)
                self.n-=1
                if len(self.chainHashTable.t)>=3*self.n:
                    self.chainHashTable.resize()
                return True
        return False
    
    def __str__(self):
        return self.cht.__str__()

'''
s = ChainedHashTableWithDuplications()
s.add(1, "a")
s.add(1, "b")
s.add(2, "c")
s.add(3, "d")
s.add(3, "e")
print(s.find(3))
s.remove(3)
print(s.find(3))
'''