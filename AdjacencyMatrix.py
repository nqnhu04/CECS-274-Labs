"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack

class AdjacencyMatrix(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros([n, n], np.bool_)
                
    def add_edge(self, i, j):
        self.a[i][j] = True
        
    def remove_edge(self, i, j):
        self.a[i][j] = False
        
    def has_edge(self, i, j):
        return self.a[i][j]

    def out_edges(self, i):
        l = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(i,j):
                l.append(j)
        return l
        
    def in_edges(self, i):
        l = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(j,i):
                l.append(j)
        return l
        
    def in_degree(self, i):
        deg = 0
        for j in range(self.n):
            if self.a[j][i]:
                deg+=1
        return deg
        
    def out_degree(self, i):
        deg = 0
        for j in range(self.n):
            if self.a[i][j]:
                deg+=1
        return deg

    def size(self) -> int :
        return self.n
                  
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.has_edge(i,j):
                    s += f"{i,j}"
        return s

'''
g = AdjacencyMatrix(4)
g.remove_edge(2,3)
print(g.has_edge(2,3))
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(0, 2)
print(g.has_edge(0,1))
print(g.has_edge(1,3))
print(g.in_edges(2))
print(g.out_edges(0))
'''
