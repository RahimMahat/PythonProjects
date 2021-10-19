# quick sort using hoare's partition

from hoare_partition import hoarePartition

def qSort(arr, l, h):
    if l < h:
        p = hoarePartition(arr, l, h)
        qSort(arr, l, p)
        qSort(arr, p+1, h)
    return arr

if __name__ == '__main__':
    arr = [8,4,7,9,3,10,5]
    print(qSort(arr,0,len(arr) - 1))