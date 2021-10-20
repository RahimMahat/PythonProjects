# stack using singly linked list
import math

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None
    
class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz = self.sz + 1

    def size(self):
        return self.sz
        
    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.key

    def pop(self):
        if self.head == None:
            return math.inf
        res = self.head.key
        self.head = self.head.next
        self.sz = self.sz - 1
        return res

s = MyStack()
s.push(10)
s.push(20)
print(s.peek())
print(s.pop())
print(s.size())
    