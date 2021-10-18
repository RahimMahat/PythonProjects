

def binary_search(l, n):
    
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == n:
            return mid
        elif l[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    # Time complexity: bigO(logn)
    # auxiliary space: bigO(1)


l = [10,20,30,40,50,60,70,80,90]
print(binary_search(l, 80))