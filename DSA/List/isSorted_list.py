# check wheather the given list is sorted or not
# i/p: [10,20,30] => o/p: true 

def is_sorted(l):
    if len(l) == 0:
        return True
    x = l[0]
    for i in l[1:]:
        if i >= x:
            return True
        else:
            return False
        

l = [58,67,89]
if is_sorted(l):
    print('Yes')
if not is_sorted(l):
    print('No')