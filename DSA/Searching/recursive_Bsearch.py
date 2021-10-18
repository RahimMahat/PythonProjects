

def bSearch(l, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if l[mid] == x:
        return mid
    elif l[mid] > x:
        return bSearch(l,x, low, mid-1)
    else:
        return bSearch(l,x, mid+1, high)
    # Time complexity: bigO(logn)
    # auxiliary space: bigO(logn)

l = [10,20,30,40,50,60]
print(bSearch(l, 70, 0, (len(l)-1)))