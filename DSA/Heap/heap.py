import math

class MyMinHeap:
    def __init__(self, l=[]):
        self.arr = []
        # build Heap constructor
        # if a list is given
        self.arr = l
        i = (len(l) - 2) // 2
        while i >= 0:
            self.minHeapify(i)
            i -= 1
        # TC: bigO(n)

    def parent(self, i):
        return (i-1)//2
    def lchild(self, i):
        return (2*i+1)
    def rchild(self, i):
        return (2*i+2)

    def insert(self, x):
        arr = self.arr
        arr.append(x)
        i = len(arr) - 1
        while i > 0 and arr[self.parent(i)] > arr[i]:
            # we keep swaping until the parent of descendant is minimum
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i = p
    # TC: bigO(logn)

    # heapify fixes the heap problem when only root is voilating the rules of given heap
    def minHeapify(self, i):
        # finding the smallest
        arr = self.arr
        lt = self.lchild(i)
        rt = self.rchild(i)
        smallest = i
        n = len(arr)
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        # if smallest isn't found yet swap the element and repeat the process
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)
        # TC: bigO(logn)

    def extractMin(self):
        arr = self.arr
        n = len(arr)
        if n == 0:
            return math.inf
        res = arr[0]
        # assigning min ele. to the last ele to remove last ele.
        arr[0] = arr[n - 1]
        # removing the last ele
        arr.pop()
        # passing the root index to minHeapify as root is now violating the min Heap rules
        self.minHeapify(0)
        return res
        # TC: bigO(logn)

    def decreaseKey(self, i, x): #i is index and x is replace element
        arr = self.arr
        # replacing array index to x
        arr[i] = x
        # balance min heap condition
        while i != 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p
        # TC: bigO(logn)
    
    def deleteKey(self, i):
        n = len(self.arr)
        if i >= n:
            return
        else:
            # decreaseing given index to -infinite so it becomes the root of heap
            self.decreaseKey(i, -math.inf)
            # now extract min will delete the root key and balance(heapify) the heap
            self.extractMin()
        # TC: bigO(logn)

    