from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_resourses = CoffeeMaker()
machine_money = MoneyMachine()
coffee_menu = Menu()


def machine_on():
    order = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if order == "report":
        machine_resourses.report()
        machine_money.report()
        return machine_on()
    elif order == "off":
        return
    else:
        order_item = coffee_menu.find_drink(order)
        if machine_resourses.is_resource_sufficient(order_item) and machine_money.make_payment(order_item.cost):
            machine_resourses.make_coffee(order_item)
            return machine_on()
        else:
            return machine_on()


machine_on()