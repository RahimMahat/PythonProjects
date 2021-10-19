

from hoare_partition import hoarePartition

def qSort(arr, l, h):
    while l < h:
        p = hoarePartition(arr, l, h)
        qSort(arr, l, p)
        l = p + 1
    # many compilers do the tail call elimination or optimization internally but python doesn't
    # so if we want to do it we do it like this
    return arr

if __name__ == '__main__':
    arr = [8,4,7,9,3,10,5]
    print(qSort(arr,0,len(arr) - 1))