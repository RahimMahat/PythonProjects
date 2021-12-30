# Number factor problem using dp

# top-down approach
def numFactorMemoization(n, dp={}):
    if n in (0, 1, 2): return 1
    elif n == 3: return 2
    elif n in dp: return dp[n]
    else:
        rec1 = numFactorMemoization(n-1, dp)
        rec2 = numFactorMemoization(n-3, dp)
        rec3 = numFactorMemoization(n-4, dp)
        dp[n] = rec1 + rec2 + rec3
    return dp[n]

# bottom-up approach
def numFactorTabulation(n):
    tb = [1, 1, 1, 2]
    for i in range(4, n+1):
        tb.append(tb[i-1] + tb[i-3] + tb[i-4])

    return tb[n]



print(numFactorMemoization(5))