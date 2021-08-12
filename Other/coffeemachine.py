#?usr/bin/env python3

MENU = {
    "espresso":{
        "ingridients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingridients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingridients":{
            "water": 250,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False    
    return True


def process_coins():
    coins = float(input("Please enter coins? (espresso-1.5),(latte-2.5),(cappuccino-3.0) $"))
    return coins


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change if any {change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, that's not sufficient amount.\nPlease pay correctly: {drink_cost} ")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕, Enjoy!")


is_on = True
while is_on:
    coffee = input("Your choice of coffee? (espresso,latte,cappuccino)  ")
    if coffee == "off":
        is_on = False
    elif coffee == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee]
        if is_resource_sufficient(drink["ingridients"]):
            pay = process_coins()
            if is_transaction_successful(pay,drink["cost"]):
                make_coffee(coffee, drink["ingridients"])


