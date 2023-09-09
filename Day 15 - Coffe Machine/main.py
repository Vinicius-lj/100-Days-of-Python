MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def att_stock(coffee):
    for ingredients in coffee["ingredients"]:
        resources[ingredients] -= coffee["ingredients"][ingredients]


def report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(choice):
    print(f"1 {choice}")
    for ingredient in choice:
        print(f"2 {ingredient}")
        if not resources[ingredient] >= choice[ingredient]:
            return ingredient
    return True


def coffe_machine():
    cash_on_hand = 0.0
    working = True
    while working:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        chosen_coffee = MENU[choice]
        if choice == "report":
            report(cash_on_hand)
        elif choice == "off":
            working = False
        elif check_resources(chosen_coffee["ingredients"]) == True:
            print("Please insert coins.")
            coins = int(input("How many quarters?: ")) * 0.25
            coins += int(input("How many dimes?: ")) * 0.1
            coins += int(input("How many nickles?: ")) * 0.05
            coins += int(input("How many pennies?: ")) * 0.01
            change = round(coins - chosen_coffee["cost"], 2)
            if change >= 0:
                print(f"Here is {change} in change")
                print(f"Here is your {choice} ☕. Enjoy!")
                cash_on_hand += chosen_coffee["cost"]
                att_stock(chosen_coffee)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            miss_resource = check_resources(chosen_coffee["ingredients"])
            print(f"Sorry there is not enough {miss_resource}")


coffe_machine()
