

def selection_sort(l):
    n = len(l)
    for i in range(n - 1):
        min_ind = i
        for j in range(i+1, n):
            if l[j] < l[min_ind]:
                min_ind = j

        l[min_ind],l[i] = l[i], l[min_ind]


    return l
    # time complexity: theta(n^2)

l = [10,40,20,30,60,50,70]
print(selection_sort(l))