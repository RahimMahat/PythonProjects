# check for palindrome 
# i/p: 'abba'  -> 'abba' => o/p: Yes

s = input('string: ')
# if s == s[::-1]:
#     print('Yes')
# else:
#     print('No')


low = 0
high = len(s) - 1
while low < high:
    if s[low] != s[high]:
        print('No')
        break
    low += 1
    high -= 1
else:
    print('Yes')