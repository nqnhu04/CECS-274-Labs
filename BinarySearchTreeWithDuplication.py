from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        w = self.binaryTree.r
        z = self.binaryTree.nil
        while w!=self.binaryTree.nil:
            if x<w.x:
                z = w
                w = w.left
            elif x>w.x:
                w = w.right
            else:
                return w.v
        if z==self.binaryTree.nil:
            return self.binaryTree.nil
        return z.v

    def add(self, key : object, value : object) -> bool:
        list=[]
        if self.find(key)!=self.binaryTree.nil:
            list=self.find(key)
            list+=value
        else:
            list+=value
            value=list
        self.binaryTree.add(key, value) 
        self.n+=1
        return True 
    
    def remove(self, x : object) -> bool:
        if self.n==0:
            raise IndexError()
        self.n-=1
        return self.binaryTree.remove(x)

q = BinarySearchTreeWithDuplication()
q.add(1, "a")
q.add(1, "b")
q.add(1, "c")
q.add(2, "d")
q.add(3, "e")
q.add(3, "z")
print(q.find(1))
print(q.find(2))
print(q.find(3))