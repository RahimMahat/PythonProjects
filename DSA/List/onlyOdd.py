# find the number which occurs odd times
# i/p: [10,30,30,10,30,30,20] => o/p: 20

def findOdd(l):
    # first method:
    # res = None 
    # for x in l:
    #     count = l.count(x)
    #     if count % 2 != 0:
    #         res = x
    #         break
    # efficient method: 
    res = 0
    for x in l:
        res = res ^ x
    return res

l = [10,30,30,10,30,30,20,20,10,10,30]
print(findOdd(l))