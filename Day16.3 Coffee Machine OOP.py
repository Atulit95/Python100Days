# Create Coffee Machine program based on OOP using packages mentioned below
# 1.cofee_maker.py
# 2.menu.py
# 3.money_machine.py

#Use Coffee_Machine_Classes_Documentation.pdf for details of pakages


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()



is_on=True
while is_on==True:
    options = menu.get_items()
    choice = input(f"​What would you like? ({options}): ")
    if choice=='off':
        is_on=False
    elif choice=='report':
        coffee_maker.report()
        moneymachine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)