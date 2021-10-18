# i/p: l=[10,20,20,20,30,30], x = 20 => o/p:3

from firstEle_index import first_index
from lastEle_index import last_index

def countOcc(l, x):
    first = first_index(l, x)
    if first == -1:
        return 0
    else:
        return last_index(l, x) - first + 1
    # time complexity: bigO(logn)

l=[10,20,20,20,30,30]
x = 20
# count = 0
# for i in l:
#     if i == x:
#         count += 1
#     # for this time complexity becomes: bigO(n)
# print(count)
print(countOcc(l, x))