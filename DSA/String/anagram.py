# check for anagram
# i/p: s1 ='listen', s2='silent' => o/p: Yes
# i/p: s1='aab', s2'abb' => o/p: No

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    # Naive method: -> time complexity: bigO(nlogn)
    # s1 = sorted(s1)
    # s2 = sorted(s2)
    # return (s1 == s2)

    # efficient method: time complexity: theta(n)
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    
    for x in count:
        if x != 0:
            return False
    return True


    

s1 = 'abaac'
s2 = 'aacba'
print(check_anagram(s1, s2))