

from merge_subarrays import merge

def merge_sort(arr, l, r):
    if r > l:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)
    # Time complexity: bigO(nlogn)
    return arr

arr = [10, 5, 30, 15, 7]
print(merge_sort(arr, 0, 4))