# quick sort using lomuto partition

from lomuto_partition import lomutoPartition

def qSort(arr, l, h):
    if l < h:
        p = lomutoPartition(arr, l, h)
        qSort(arr, l, p-1)
        qSort(arr, p+1, h)
    return arr

if __name__ == '__main__':
    arr = [8,4,7,9,3,10,5]
    print(qSort(arr,0,len(arr) - 1))