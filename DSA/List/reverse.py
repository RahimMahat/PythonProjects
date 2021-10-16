# reverse the given list
#i/p: l = [10,20,30,40] => o/p: rev = [40,30,20,10]

def get_reverse(l):
    s = 0
    e = len(l) - 1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1
    return l 

l = [10,20,30,40,23]
print(get_reverse(l))