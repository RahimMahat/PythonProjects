# find the distinct element in the list 
# i/p: l= [10,20,10,30,30,20] => o/p: 3

def solution(l):
    # method 1:
    # res = []
    # for i in l:
    #     if i not in res:
    #         res.append(i)
    # return len(res)
    # method 2:
    # res = 1
    # for i in range(1,len(l)):
    #     if l[i] not in l[0:i]:
    #         res += 1
    # return res

    # efficient method
    s = set(l)
    return len(s)

l= [10,10,10,20]
print(solution(l))