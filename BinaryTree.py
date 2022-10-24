import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, key, value) :
            self.x = key
            self.v = value

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        if u == self.nil:
            return -1
        d = 0
        while u!=self.r:
            u = u.parent
            d+=1
        return d

    def size(self) -> int:
        return self._size(self.r)
    
    def _size(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        u = self.r
        prv = self.nil
        n = 0
        while u!=self.nil:
            if prv == u.parent:
                n+=1
                if u.left!=self.nil:
                    nxt = u.left
                elif u.right!=self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right!=self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return n

    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u : Node):
        if u == self.nil: return
        self.traverse(u.left)
        self.traverse(u.right)

    def traverse2(self):
        u = self.r
        prv = self.nil
        while u!=self.nil:
            if prv == u.parent:
                if u.left!=self.nil:
                    nxt = u.left
                elif u.right!=self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right!=self.nil:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        if self.r!=self.nil:
            q.add(self.r)
        while q.size()>0:
            u = q.remove()
            print(f"{u.x}: {u.v}")
            if u.left!=self.nil:
                q.add(u.left)
            if u.right!=self.nil:
                q.add(u.right)
            
    def first_node(self):
        w = self.r
        if w == self.nil: 
            return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    
    def in_order(self) :
        self._in_order(self.r)
    
    def _in_order(self, u : Node):
        if u.left!=self.nil:
            self._in_order(u.left)
        print(f"{u.x}: {u.v}")
        if u.right!=self.nil:
            self._in_order(u.right)

    def pre_order(self) :
        self._pre_order(self.r)

    def _pre_order(self, u : Node):
        print(f"{u.x}: {u.v}")
        if u.left!=self.nil:
            self._pre_order(u.left)
        if u.right!=self.nil:
            self._pre_order(u.right)

    def post_order(self) :
        self._post_order(self.r)
    
    def _post_order(self, u : Node):
        if u.left!=self.nil:
            self._post_order(u.left)
        if u.right!=self.nil:
            self._post_order(u.right)
        print(f"{u.x}: {u.v}")

    def __str__(self):
        l = []
        self.in_order()
        return ', '.join(map(str, l))