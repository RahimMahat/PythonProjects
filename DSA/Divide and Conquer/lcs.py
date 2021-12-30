'''
Longest Common Sequence
- s1 and s2 are given strings
- find the length of the longest subsequence which is common to both strings
- subsequence a sequence that can be driven from another sequence by deleting some elements without changing the order of them
Example
I/P: s1 = "elephant", s2 = "erepat"
O/P: 5
Explanation: "eepat"
'''

def lcs(s1, s2, index1, index2):
    # if we reach to the end of string return 0
    if index1 == len(s1) or index2 == len(s2):
        return 0
    # if the chars are matching then move to the next chars
    if s1[index1] == s2[index2]:
        return 1 + lcs(s1, s2, index1+1, index2+1)
    else:
    # otherwise move to the next char of second string
        op1 = lcs(s1, s2, index1, index2+1)
    # or next char of the first string if the chars are not matching
        op2 = lcs(s1, s2, index1+1, index2)
    # and return the maximum from them
        return max(op1, op2)

s1, s2 = "elephant", "erepat"
print(lcs(s1, s2, 0, 0))