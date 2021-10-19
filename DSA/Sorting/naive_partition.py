

def naive_partition(arr, p):
    n = len(arr)
    arr[p], arr[n-1] = arr[n-1], arr[p]
    temp = []
    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)
    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
    for i in range(len(arr)):
        arr[i] = temp[i]
    # time complexity: theta(n), auxiliary space: theta(n)
    return arr

if __name__ == '__main__':
    arr = [5,13,6,9,12,8,11]
    p = 5
    print(naive_partition(arr, p))
