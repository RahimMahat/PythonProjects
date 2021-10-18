
def first_index(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid]  > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or l[mid-1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1
    # time complexity: bigO(logn)

if __name__ == '__main__':
    l = [10,10,20,30,40,40,50,40]
    print(first_index(l, 40))