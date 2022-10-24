import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator
import BinarySearchTree

class Calculator:
    def __init__(self) :
        self.dict = BinarySearchTree.BinarySearchTree()
        self.stack = ArrayStack.ArrayStack()

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def print_expression(self, s : str) -> str :
        t = ''
        for char in s:
            if char == "(" or char == ")" or char == "+" or char == "-" or char == "*" or char == "/":
                t+=char
            else:
                if self.dict.find(char)!=None:
                    l = self.dict.t[self.dict.hash(char)]
                    for i in range(len(l)):
                        if l[i].key == char:
                            t+=str(l[i].value)
                else:
                    t+=char
        return t

    def matched_expression(self, s : str) -> bool :
        if s == "":
            return True
        for char in s:
            if char == "(":
                self.stack.push(char)
            else:
                if char == ")":
                    if self.stack:
                        self.stack.pop()
                    else:
                        return False       
        if not self.stack:
            return True
        return False


    def build_parse_tree(self, exp : str) ->str:
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node("")
        u = t.r
        operators = ["+", "-", "*", "/"]
        for char in exp:
            if char == "(":
                u = u.insert_left()
            elif char == ")":
                if u.parent!=None:
                    u=u.parent
            elif char in operators:
                u.x = char
                u = u.insert_right()
            elif char not in operators:
                u.x = char
                u = u.parent
        return t
        
    def _evaluate(self, u):
        op = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        if u.left!=None and u.right!=None:
            fn = op[u.x]
            return fn(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left==None and u.right==None:
            t = self.dict.find(u.x)
            if t!=None:
                return t
            return u.x
        else:
            if u.left!=None:
                return self._evaluate(u.left)
            else:
                return self._evaluate(u.right)
        return 0

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)
        except:
            return 0