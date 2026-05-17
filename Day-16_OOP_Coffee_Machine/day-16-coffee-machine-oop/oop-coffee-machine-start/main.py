from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Coffee Machine Program
coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


# Find the cost of a particular drink
# def find_cost(drink):
#     for item in menu.menu:
#         if item.name == drink:
#             print(f"The cost of {drink} is ${item.cost}")
#             return item.cost
#
#
# cost = 0

# for item in menu.menu:
#     print(f"Name: {item.name}")
#     print(f"Cost: ${item.cost}")
#     print("Ingredients:")
#     for ingredient, amount in item.ingredients.items():
#         print(f"  {ingredient}: {amount}ml")
#     print()


while True:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    choice = input(f"What would you like? ({menu.get_items()}):")
    drink = menu.find_drink(choice) # Remember, find_drink() returns an object that has attributes
    if choice == "off":
        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        exit(0)
    elif choice == "report":
        # TODO: 3. Print report.
        coffee_machine.report()  # Took the method out from the print statement
        # print(f"Money: ${money.profit}") # My implementation was overly complicated
        money.report() # This is the correct implementation
    else:
        # TODO: 4. Check resources sufficient?
        if coffee_machine.is_resource_sufficient(drink):
            # TODO: 5. Process coins.
            # TODO: 6. Check transaction successful?
            # cost = find_cost(choice) # This function was totally unnecessary
            # payment = money.make_payment(cost)
            payment = money.make_payment(drink.cost) # Tapping into the drink object's attribute (comes from MenuItem)
            # TODO: 7. Make Coffee.
            coffee_machine.make_coffee(drink)
