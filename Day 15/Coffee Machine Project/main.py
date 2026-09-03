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


coffee = True
profit = 0

while coffee:
    user_choice = input("What would you like?('espresso' ,'latte','cappuccino')\n")
    if user_choice == 'off':
        coffee = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${profit}")
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        drink = MENU[user_choice]
        ingredients = drink["ingredients"]
        cost = drink["cost"]
        resources_sufficient = True
        for item in ingredients:
            if ingredients[item] > resources[item]:
                print(f"Sorry, There's not enough {item}.")
                resources_sufficient = False
        if resources_sufficient:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            if total_coins <  cost:
                print("Sorry, you don't have enough money. Money Refund!")

            else:
                if total_coins > cost:
                    change = total_coins - cost
                    print(f"Here is ${round(change, 2)} in change.")
                profit += cost

                for item in ingredients:
                    resources[item] = resources[item] - ingredients[item]

                print(f"Here is your {user_choice}. Enjoy!")