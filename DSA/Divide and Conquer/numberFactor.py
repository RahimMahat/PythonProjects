'''
Given N, find the number of ways to express N as a sum of 1, 3, 4
Example 1:
I/P = 5
O/P = 6
Explanation: There are 6 ways we can express N -> [(4,1), (1,4), (1,3,1), (3,1,1), (1,1,3), (1,1,1,1,1)]
'''

def numberFactor(n):
    # if the number is 0, 1 or 2 there is only 1 output
    if n in (0, 1, 2):
        return 1
    # we can get 3 by tow way[(1,1,1), (3)], so return 2
    elif n == 3:
        return 2
    else:
    # else make recursive call with substracting numbers in which terms you want them to be represented, i.e 1, 3, 4
        subP1 = numberFactor(n - 1)
        subP2 = numberFactor(n - 3)
        subP3 = numberFactor(n - 4)
        # return the sum of those subproblems
        return subP1 + subP2 + subP3

n = 5
print(numberFactor(n))
