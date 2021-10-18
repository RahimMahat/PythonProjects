

def last_index(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid]  > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1
        else:
            if mid == (len(l) - 1) or l[mid] != l[mid+1]:
                return mid
            else:
                low = mid + 1
    return -1

    
if __name__ == "__main__":
    l = [10,10,20,30,40,40]
    x = 40
    print(last_index(l, x))