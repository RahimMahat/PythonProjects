

def merge(l, low, mid, high):
    left = l[low : mid+1]
    right = l[mid+1 : high+1]
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        l[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        l[k] = right[j]
        j += 1
        k += 1
    # Time complexity: theta(m+n)
    return l

if __name__ == '__main__':
    l = [10,15,20,40,8,11,55]
    low = 0
    mid = 3
    high = 6
    print(merge(l, low, mid, high))