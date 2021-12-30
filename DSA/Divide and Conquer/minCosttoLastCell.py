'''
Minimum cost to reach the last cell
- 2D matrix is given
- each cell has a cost associated with it for accessing
- we need ot start from (0,0), cell and go till (n-1, n-1) cell
- we can go only to right or down cell from current cell
- find the ways in which the cost is minimum
'''

def findMinCost(twoDArrays, row, col):
    # if the row col are -1 return inf
    if row == -1 or col == -1:
        return float('inf')
    # if the row col are at the end of 2D array return cost of it
    elif row == 0 and col == 0:
        return twoDArrays[0][0]
    else:
        # go down in the array
        op1 = findMinCost(twoDArrays, row-1, col)
        # go right in the array
        op2 = findMinCost(twoDArrays, row, col-1)
        # add the cost of the traversing row col and minimum of above two operations
        return twoDArrays[row][col] + min(op1, op2)

twoDArray = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3]
]

print(findMinCost(twoDArray, 4, 4))