# given a string if there permutation string can be a palindrome return true
# i/p: s = 'geegg' <'gegeg or eggge'>these could be palindromes => o/p: True

from collections import Counter

def solution(s: str) -> bool:
    # counter return the word:frequency as key:value pair it is specially made for the counting purposes
    cnt = Counter(s)
    odd = 0 
    for freq in cnt.values():
        # checking for the odd frequency
        if freq % 2 != 0:
            odd += 1
            # checking if the odd count is more than 1 then return False
            if odd > 1:
                return False
    # if we come out of the for loop without returning we return True
    return True
    # Time complexity becomes theta(n)

s = 'geegg'
print(solution(s))