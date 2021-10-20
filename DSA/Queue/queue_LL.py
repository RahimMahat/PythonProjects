class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return (self.sz == 0)
    
    def getFront(self):
        return self.front.key
    
    def getRear(self):
        return self.rear.key
    
    def enque(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp

        self.rear = temp
        self.sz += 1
    
    def deque(self):
        if self.front == None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next
            # if there was only one element in the queue then front and rear both None
            if self.front == None:
                self.rear = None
            self.sz -= 1
            return res

q = MyQueue()
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
q.enque(50)
print(q.deque())
print(q.size())
print(q.getFront())
print(q.getRear())