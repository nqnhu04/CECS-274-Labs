from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i : int) -> Node:
        if i<self.n/2:
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:
            p = self.dummy
            for k in range(self.n-i):
                p = p.prev
        return p
        
    def get(self, i) -> np.object:
        if i<0 or i>self.n-1:
            raise IndexError()
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        if i<0 or i>self.n-1:
            raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w : Node, x : np.object) -> Node:
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n+=1
        return u
            
    def add(self, i : int, x : np.object)  :
        if i<0 or i>self.n:
            raise IndexError()
        self.add_before(self.get_node(i),x)

    def _remove(self, w : Node) :
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n-=1
    
    def remove(self, i :int) :
        if i<0 or i>=self.n:
            raise IndexError()
        self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        n, p = self.dummy.next, self.dummy.prev
        while n.x==p.x and n!=self.dummy:
            n, p = n.next, p.prev
        return n==self.dummy

    def reverse(self) :
        if not self:
            raise IndexError()
        c = self.dummy
        for i in range(self.n+1):
            t=c.prev
            n=c.next
            c.prev, c.next = c.next, t
            c=n
         
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"
        

    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise IndexError("Not implemented. Please use the references next and prev")
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
