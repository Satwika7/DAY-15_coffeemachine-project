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
profit=0
on = True
while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        on = False
    elif user_choice == "report":
        for key in resources:
            if resources[key]<0:
                resources[key]=0
            print(f"{key}: {resources[key]}")
        print(f"current profit is {profit}.")
    else:
        not_suff = []
        not_sufficient = 0
        val = MENU[user_choice]["ingredients"]
        for ing in val:
            resources[ing] -= val[ing]
            if resources[ing] < 0:
                not_suff.append(ing)
                not_sufficient += 1
        if not_sufficient > 0:
            for i in not_suff:
                print(f"sorry there is not enough {i}.")
            for ing in val:
                resources[ing] += val[ing]
        else:
            print("please insert coins.")
            profit += MENU[user_choice]["cost"]
            quarters = int(input("How many Quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_cost = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
            if total_cost < MENU[user_choice]["cost"]:
                print("sorry that's not enough money, Money refunded.")
                for ing in val:
                    resources[ing] += val[ing]
            else:
                change = round(total_cost - MENU[user_choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your your {user_choice} enjoy!.")