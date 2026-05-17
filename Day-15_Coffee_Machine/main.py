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

profits = 0

while True:

    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    def prompt_drink():
        return input(" What would you like? (espresso/latte/cappuccino): ")


    drink_input = prompt_drink()

    # TODO: 3. Print report to show current resources and profits
    while drink_input == "report":
        for key in resources:
            print(f"{key.title()}: {resources[key]} mL")  # Capitalizes first letter, returns key-value pairs strings
        print(f"Profits: ${profits}")
        drink_input = prompt_drink()

    # TODO: 2. Turn off the Coffee Machine by entering “off”
    if drink_input == "off":
        exit(0)


    # TODO: 4. Check resources sufficient?
    def check_resources(drink):
        """Will check each required ingredient in turn for the supplied drink parameter and
        return True or False depending on the available resources."""
        ingredients = MENU[drink]["ingredients"]
        for ingredient in ingredients:
            if ingredient in resources:
                if resources[ingredient] < ingredients[ingredient]:
                    print(f" Sorry, there is not enough {ingredient}")
                    return False
        return True


    # TODO: 5. Process coins
    dollars_amount = 0  # Amount of dollars received in coins


    def process_coins(quarters, dimes, nickels, pennies):
        """Takes the coins and calculates the amount of dollars"""
        dollars = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return round(dollars, 2)

    enough_resources = check_resources(drink_input)
    if enough_resources:
        print("Please insert coins.")
        quarters_amount = int(input("how many quarters?: "))
        dimes_amount = int(input("how many dimes?: "))
        nickels_amount = int(input("how many nickels?: "))
        pennies_amount = int(input("how many pennies?: "))
        dollars_amount = process_coins(quarters_amount, dimes_amount, nickels_amount, pennies_amount)
        # print(f"${process_coins(quarters_amount, dimes_amount, nickels_amount, pennies_amount)}")

    # TODO: 6. Check transaction successful (enough money)?
    cost = MENU[drink_input]["cost"]


    def check_transaction():
        if dollars_amount >= cost:
            change = dollars_amount - cost
            if change == 0:
                return True
            else:
                print(f"Here is ${round(change, 2)} in change.")
                return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


    if enough_resources:
        enough_money = check_transaction()


    # TODO: 7. Make Coffee, update resources and profits
    def make_coffee(drink):
        global profits
        """Will check each required ingredient in turn for the supplied drink parameter and
            update resources accordingly."""
        ingredients = MENU[drink]["ingredients"]
        for ingredient in ingredients:
            if ingredient in resources:
                updated_ingredient = resources[ingredient] - ingredients[ingredient]
                resources.update({ingredient: updated_ingredient})
        profits = profits + cost


    if enough_money and enough_resources:
        make_coffee(drink_input)
        print(f"Here is your {drink_input} ☕. Enjoy!")
