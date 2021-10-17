class MyHash:

    def __init__(self, c):
        self.cap = c
        # making the table of empty slot of size as given value
        self.table = [-1] * c
        # initializing size with 0 to indicate space
        self.size = 0

    def hash(self, x):
        return x % self.cap

    def search(self, x):
        # first we compute the has of the key
        h = self.hash(x)
        t = self.table
        i = h
        # running the loop until we find an empty slot (-1 is to indicate the empty slot)
        while t[i] != -1:
            # if we find the key stop the search
            if t[i] == x:
                return True
            # using linear probing in this case
            i = (i+1) % self.cap
            # if we traverse back to the starting position we stop the loop
            if i == h:
                return False
        # if we don't find the key even from iterating over the table we return false
        return False

    def insert(self, x):
        # if the size is full return false
        if self.size == self.cap:
            return False
        # if the key already exists return false
        if self.search(x) == True:
            return False
        # compute hash of the key
        i = self.hash(x)
        t = self.table
        # finding the empty slot or deleted slot (-1 = empty, -2 = deleted)
        while t[i] not in (-1, -2):
            i = (i+1) % self.cap
        # once we have the index we insert the key there
        t[i] = x
        # increase the table size
        self.size = self.size + 1
        # and return True
        return True
    
    def remove(self, x):
        # same as of search function with one change
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                # we make the element at found index -2 to indicate it's deleted
                t[i] = -2
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False

h = MyHash(2)

h.insert(34)
h.insert(21)
print(h.search(21))
h.remove(21)
print(h.search(21))