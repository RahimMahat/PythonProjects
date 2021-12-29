'''
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight
is less than or equal to a given limit and the total value is as large as possible
'''


class Item:
    def __init__(self, weight, value): 
        self.weight = weight
        self.value = value
        # calculate the density or ratio for each item
        self.ratio = value / weight

def knapSack(items, capacity):
    # sort the items based on their ratio in descending order
    items.sort(key= lambda x: x.ratio, reverse=True)
    # variables to keep track of used capacity and total value
    usedCap = 0
    totalVal = 0
    # iterate through the items array
    for item in items:
        # if used capacity + weight of item is less or equal to total capacity
        if usedCap + item.weight <= capacity:
            # then add the item weight to used capcity
            usedCap += item.weight
            # and item value to the total value
            totalVal += item.value
        # else sum the fraction of the item
        else:
            # find unused weight 
            unusedWeight = capacity - usedCap
            # add it to the used capacity
            usedCap += unusedWeight
            # using the expression above in the class find value
            value = item.ratio * unusedWeight
            # add it to the total value
            totalVal += value
        
        if usedCap == capacity:
            break
    
    print(f"Total value after knapSack is: {totalVal}")


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
itemsList = [item1, item2, item3]

knapSack(itemsList, 70)
