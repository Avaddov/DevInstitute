def employee_info(name, salary=9000):
    print(f'the employees name is {name} and their salary is {salary}')


employee_info("Bob", 10000)



def day_of_week(num):
    if num == 1:
        print("sunday")

    elif num == 2:
        print("monday")
    elif num == 3:
        print("tuesday")
    elif num == 4:
        print("wednesday")
    elif num == 5:
        print("thursday")
    elif num == 6:
        print("friday")
    elif num == 7:
        print("saturday")
    elif num <1 or num > 7:
        print('none')
    
day_of_week(3)




# Lets simulate a trafic light.
# Write a function that takes a color as a parameter
# Depending on which color was chosen (red, yellow, green) print a response (stop, slow down, go).

def trafic_light(color):

    if color == "red" or "Red":
        print("STOP says the red light!")
    elif color == "green" or "Green":
        print("GO says the green")    
    elif color == "yellow" or"Yellow":
        print("Slow says the yellow light blinking in between")
    elif color == "fire" or "FIRE":
        print("KNEEL SAYS THE DEMON LIGHT WITH ITS EYE OF COAL! SAURON KNOWS YOUR LICENSE PLATE AND STARES INTO YOUR SOUL!")
    else:
        print("none")

trafic_light("Red")



# create a function that takes a list of names as a parameter and prints out a new list with all the names that begin with the letter a

def names_list(names):
    a_names = []
    for name in names:
        if name[0] == 'a':
            a_names.append(name)
        print(a_names)

names_list(['chaim', 'anna', 'dan', 'aviva'])
    
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class = Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width



The purpose of this exercise is to create a menu of a restaurant. As a Manager we will be able to add and delete dishes.

# 1. Create a python file called *menu_manager.py*

# 2. Create a class called `MenuManager`.

# 3. Create a method `__init__` that instantiates an attribute called `menu`. This variable is a **list of dictionaries** that contains dishes. Each dish has a name, a price, a spice level and a gluten index (this key is a boolean).
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

# Translate this information into the `menu` attribute.
# 4. Create a method called `add_item(name, price, spice, gluten)`. This method adds the new dish in the menu.

# 5. Create a method called `update_item(name, price, spice, gluten)`. 
# t checks if the dish is in the menu, if it is, then update it. If it isn't, send a message to the manager

# 6. Create a method called `remove_item(name)`. 
# It has to check if the dish is in the menu, if it is, then delete it and print the dictionary. If it isn't, send a message to the manager.

