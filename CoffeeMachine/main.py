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

money = 0

print(MENU["espresso"]["ingredients"]["water"])



while True:
    choice = input("What drink would you like? (espresso / latte / cappuccino): ").lower()

    if choice == "espresso": 
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU ["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            money += MENU["espresso"]["cost"]
            print("Here is your espresso! Enjoy your drink.")
        else:
            print("Sorry, not enough resources.")
        
    elif choice == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"] and MENU ["latte"]["ingredients"]["coffee"]<= resources["coffee"]:
            MENU["latte"]["ingredients"]["water"] -= resources["water"]
            MENU["latte"]["ingredients"]["milk"] -= resources["milk"]
            MENU ["latte"]["ingredients"]["coffee"]-= resources["coffee"]
            money += MENU["latte"]["cost"]

            print("Here is your latte! Enjoy your drink.")
        else:
            print("Sorry, not enough resources.")
        
    elif choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"] and MENU ["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
            MENU["cappuccino"]["ingredients"]["water"] -= resources["water"]
            MENU["cappuccino"]["ingredients"]["milk"] -= resources["milk"]
            MENU ["cappuccino"]["ingredients"]["coffee"]-= resources["coffee"]
            money += MENU["cappuccino"]["cost"]
            print("Here is your cappuccino! Enjoy your drink.")
        else:
            print("Sorry, not enough resources.")
        
    elif choice == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money : {money}$")
        
    elif choice == "off":
        break

    else:
        print("Incorrect input. Please spell the coffee correctly.")


