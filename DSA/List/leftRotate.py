# left rotate a list by one
# i/p: l = [10,20,30,40] => o/p: l = [20,30,40,10]

# def leftRotate_byOne(l):
#     n = len(l)
#     x = l[0]
#     for i in range(1,n):
#         l[i-1] = l[i]
#     l[n-1] = x
#     return l 
    

# direct methods:
# 1
# l = l[1:] + l[0:1]
# return l
# 2
# l.append(l.pop(0))
# return l
# print(leftRotate_byOne(l))


# left rotate a list by d places
# i/p: l = [10,20,30,40], d = 2 => o/p: l = [30,40,10,20]

def leftRotate_byDigit(l, d):
    for i in range(0,d):
        l.append(l.pop(0))
    return l # time complexity = theta(nd)


l = [10,20,30,40]
d = 2
print(leftRotate_byDigit(l, d))


# direct method:
# 1
# l = l[d:] + l[:d]
# 2
# from collections import deque
# dq = deque(l)
# dq.rotate(-d)
# l = list(dq)
# print(l)