'''
- you are only allowed to traverse the grid
- with right and down position
- and find the number of paths we can take to traverse from start to end
- given the numbers of rows and columns of the grid (dimensions)
- if one of the dimension is 0 then the grid becomes invalid so return 0
e.g gridTraveler(2,3) -> 3
'''

def gridTraveler(m, n, memo={}):
    # recursive approach:
    # if m == 1 and n == 1: return 1
    # if m == 0 or n == 0: return 0
    # return gridTraveler(n-1, m) + gridTraveler(n, m-1)
    # TC: bigO(2^m+n), Space complexity: bigO(n + m)

    # DP approach:
    # memo dict holds the m,n coordinates as key and return value as value
    key = f'{m},{n}'
    if key in memo: return memo[key]
    # for 1x1 grid only 1 way of traversal
    if m == 1 and n == 1: return 1
    # for 1x0 or 0x1 grid is invalid so return 0
    if m == 0 or n == 0: return 0
    # move right columns are reduced by one move down rows are reduced by one return the addition
    memo[key] = gridTraveler(m, n-1, memo) + gridTraveler(m-1, n, memo)
    return memo[key]

    # TC: bigO(m *n), Space complexity: bigO(n + m)



print(gridTraveler(2,3))    # 3
print(gridTraveler(1,1))    # 1 
print(gridTraveler(1,3))    # 1
print(gridTraveler(18,18))  # 2333606220
print(gridTraveler(20,18))  # 8597496600

    