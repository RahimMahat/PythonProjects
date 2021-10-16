# find the second largest number in the list
# i/p: l1 = [10,5,8,20]  => o/p: 10

def getSecMax(l):
    # naive method: 
    # if len(l) <= 1:
    #     return None
    # largest = max(l)
    # sec_lar = None
    # for x in l:
    #     if x != largest:
    #         if sec_lar == None:
    #             sec_lar = x
    #         else : 
    #             sec_lar = max(sec_lar, x)
    # worst time complexity -> theta(n)
    # return sec_lar

    # efficient method:
    if len(l) <= 1:
        return None
    largest = l[0]
    sec_lar = None 
    for x in l[1:]:
        if x > largest:
            sec_lar = largest
            largest = x
        elif x != largest:
            if sec_lar == None or sec_lar < x:
                sec_lar = x
    # time complexity -> theta(n)
    return sec_lar 


l1 = [20,89,67,98,77]
secMax = getSecMax(l1)
print(secMax)