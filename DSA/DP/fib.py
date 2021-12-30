def fib(n, memo={}):
    # recurse approach:
    # if n <= 2: return 1
    # return fib(n-1) + fib(n-2)
    # TC: bigO(2^n), Space complexity: bigO(n)

    # DP approach:
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

    # TC: bigO(n), Space complexity: bigO(n)

print(fib(70))