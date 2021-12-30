'''
Longest Palindromic Subsequence
- s is given
- find the longest palindromic subsequence
- palindrome is a string that reads the same backward as well as forward
Example
I/P: "ELRMENMET"
O/P: 5
Explanation: "EMEME'
'''

def lps(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    if startIndex == endIndex:
        return 1
    if s[startIndex] == s[endIndex]:
        return 2 + lps(s, startIndex+1, endIndex-1)
    else:
        op1 = lps(s, startIndex, endIndex-1)
        op2 = lps(s, startIndex+1, endIndex)
        return max(op1, op2)

s = "ELRMENMET"
print(lps(s, 0, len(s)-1))