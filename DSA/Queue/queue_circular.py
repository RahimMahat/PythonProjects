# queue circular list implementation 

class MyQueue:
    def __init__(self, C):
        self.l = [None] * C
        self.cap = C
        self.size = 0
        self.front = 0
    
    def getFront(self):
        if self.size == 0:
            return None
        else:
            return self.l[self.front]
        
    def getRear(self):
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size - 1) % self.cap
            return self.l[rear]

    def isEmpty(self):
        return (self.size == 0)
    
    def isFull(self):
        return (self.size == self.cap)
    
    def getSize(self):
        return self.size
        
    def enque(self, x):
        if self.size == self.cap:
            return
        else:
            rear = (self.front + self.size - 1) % self.cap
            rear = (rear + 1) % self.cap
            self.l[rear] = x
            self.size += 1
        
    def deque(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return res
        
    # circular implementation of queue with TC: bigO(1)

q = MyQueue(4)
q.enque(10)
q.enque(10)
q.enque(10)
q.deque()

print(q.isEmpty())
print(q.getSize())
print(q.isFull())