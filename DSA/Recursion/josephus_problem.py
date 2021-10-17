# i/p: n = 7, k = 3  => o/p: 3
# i/p: n = 8, k = 2  =? o/p: 0

def jos(n, k):
    if n == 1:
        return 0

    return (jos(n-1, k) + k) % n
    # time complexity is: theta(n)

def josBeginWithOne(n, k):
    # if the numbering of seats begin with 1 instead of 0
    return jos(n, k) + 1

print(jos(8, 2))