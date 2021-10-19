

def merge(a, b):
    # naive method:
    # res = a + b
    # res.sort()
    # # Time complexity: bigO((m+n)*log(m+n))
    # return res 

    # efficient method:
    res = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < m:
        res.append(a[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1
    # Time complexity: theta(m+n)
    return res




a = [10,15,30]
b = [2,20]
print(merge(a, b))