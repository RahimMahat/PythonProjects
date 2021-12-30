'''
- S1 and S2 are given strings
- Convert S2 to S1 using delete, insert or replace operations
- find the minimum count of edit operations
Example:
I/P : S1 = "table", S2 = "tbrles"
O/P : 3
'''

def findMinOps(s1, s2, index1, index2):
    # if you've reached at the end of the first string
    if index1 == len(s1):
        # delete all remaining chars
        return len(s2) - index2
    # if you've reached at the end of second string
    if index2 == len(s2):
        # insert all remaining chars
        return len(s1) - index1
    # if the chars of both string match move to the next index
    if s1[index1] == s2[index2]:
        return findMinOps(s1, s2, index1+1, index2+1)
    else:
        # find the cost of individual operations
        deleteOp = 1 + findMinOps(s1, s2, index1, index2+1)
        insertOp = 1 + findMinOps(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOps(s1, s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)

s1, s2, = "table", "tbrles"
print(findMinOps(s1, s2, 0, 0))


