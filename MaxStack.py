from Interfaces import Stack
import SLLStack


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        self.maxSt = SLLStack.SLLStack()
        
    def max(self) ->object:
        '''
            Returns the max element
        '''
        if not self.maxSt:
            raise IndexError
        return self.maxSt.head.x
    
    def push(self, x : object) : 
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
        '''
        max = x
        if self.maxSt and max<self.maxSt.head.x:
            max = self.maxSt.head.x
        self.stack.push(x)
        self.maxSt.push(max)

    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
        '''
        u = self.stack.pop()
        self.maxSt.pop()
        return u

    def size(self) -> int:
        return self.stack.size()

'''
s = MaxStack()
s.push(3)
s.push(1)
s.push(4)
s.push(2)
print(s.max())
print(s.pop())
print(s.pop())
print(s.max())
print(s.pop())
print(s.max())
'''