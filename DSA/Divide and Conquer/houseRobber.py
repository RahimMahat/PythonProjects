'''
- Given N number of houses along the street with some amount of money
- Adjacent houses cannot be stolen
- Find the maximum amount that can be stolen
Example:
I/P = [6, 7, 1, 30, 8, 2, 4]
O/P = 41
Explanation: Stolen houses are -> [7, 30, 4]
'''

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFirstHouse = houseRobber(houses, currentIndex + 1)
        return max(skipFirstHouse, stealFirstHouse)

houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0))