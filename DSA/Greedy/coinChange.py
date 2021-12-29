'''
You are given coins of different denominations and total amount of money. Find the minimum number of coins
that you need to make up the given amount
'''

def coinChange(amount, coins):
    total = amount
    coins.sort()
    index = len(coins) - 1
    while True:
        coinVal = coins[index]
        if total >= coinVal:
            print(coinVal, end=" ")
            total -= coinVal
        else:
            index -= 1
        
        if total == 0:
            break

coins = [1,12,5,3,7,34,9,100]
totalAmount = 77
coinChange(totalAmount, coins)