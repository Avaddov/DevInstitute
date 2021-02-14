# The purpose of this exercise is to create a menu of a restaurant. As a Manager we will be able to add and delete dishes.

# 1. Create a python file called *menu_manager.py*

# 2. Create a class called `MenuManager`.
class MenuManager ():
	def __init__(self, menu)

# Each dish has a name, a price, a spice level and a gluten index (this key is a boolean).
# Below, are the dishes currently offered to the customers.

# Soup – 10 – B - False
# Hamburger – 15 - A - True
# Salad – 18 - A - False
# French Fries – 5 - C - False
# Beef bourguignon– 25 - B - True
# Meaning: For the spice level:
#    • A = not spicy,
#    • B = a little spicy,
#    • C = very spicy

    menu = [
        {"dish": "soup", "price": "10", "spice level": "B", "Gluten": False},
        {"dish": "hamburger", "price": "15", "spice level": "A", "Gluten": True},
        {"dish": "salad", "price": "18", "spice level": "A", "Gluten": False},
        {"dish": "spicy fries", "price": "5", "spice level": "C", "Gluten": False},
        {"dish": "Beef bourguignon", "price": "25", "spice level": "B", "Gluten": True}
    ]

# Translate this information into the `menu` attribute.
# 4. Create a method called `add_item(name, price, spice, gluten)`. This method adds the new dish in the menu.

def add_item(name, price, spice, gluten)

# 5. Create a method called `update_item(name, price, spice, gluten)`.
# t checks if the dish is in the menu, if it is, then update it. If it isn't, send a message to the manager

# 6. Create a method called `remove_item(name)`.
# It has to check if the dish is in the menu, if it is, then delete it and print the dictionary. If it isn't, send a message to the manager.
