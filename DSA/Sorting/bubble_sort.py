
def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
    # time complexity: bigO(n^2)

l = [10,40,20,30,60,50,70]
print(bubble_sort(l))
