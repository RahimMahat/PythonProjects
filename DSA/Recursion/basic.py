#1. print n ot 1 using recursion

# def N_to_1(n):
#     if n <= 0:
#         return
#     print(n)
#     N_to_1(n-1)

# N_to_1(3)

#2. print 1 ot n using recursion

# def One_to_N(n):
#     if n == 0:
#         return
#     One_to_N(n - 1)
#     print(n)

# One_to_N(3)

#3. Sum of digits using recursion
# i/p: 253 => o/p: 10 (2+5+3)

def dSum(n):
    if n < 10:
        return n   

    return dSum(n//10) + n % 10

print(dSum(753))