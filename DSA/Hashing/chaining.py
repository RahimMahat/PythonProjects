class MyHash:

    def __init__(self, b):
        self.BUCKET = b 
        # making an empty hash table [list of list]
        self.table = [[] for x in range(b)]
    
    def insert(self, x):
        i = x % self.BUCKET
        # find the key(index) in hash table and store it in that index
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        # finding the index of the number to remove from the list
        self.table[i].remove(x)

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]

# Example:
# BUCKET = 7 
# table = [[],[],[],[],[],[],[]] -> initial state
h = MyHash(7)
# table = [[70,56], [71], [9,72],[],[],[],[]]
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)

print(h.search(56)) # -> True

h.remove(56)

print(h.search(56)) # -> False