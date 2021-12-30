# House Robber problem using dp

# top-down approach
def houseRobberMemoization(houses, currentIndex, dp={}):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in dp:
            stealFirstHouse = houses[currentIndex] + houseRobberMemoization(houses, currentIndex+2, dp)
            skipFirstHouse = houseRobberMemoization(houses, currentIndex+1, dp)
            dp[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return dp[currentIndex]

# bottom-up approach
def houseRobberTabulation(houses, currentIndex):
    tb = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        tb[i] = max(houses[i]+tb[i+2], tb[i+1])

    return tb[0]


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobberTabulation(houses, 0))
