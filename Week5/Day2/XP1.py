# Exercise 1 : Pets
# Consider this code

class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

        # Add another cat breed


class Sphynx(Cat):
    def walk(self):
        return f'{self.name} is doing cat things'


# Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
cat1 = Bengal("Mizuki", 7)
cat2 = Chartreux("Fluffy", 4)
cat3 = Sphynx("Beerus", 10)
my_cats = [cat1, cat2, cat3]
# Instantiate the Pet class with all your cats. Use the variable my_pets
my_pets = Pets(my_cats)
# Output all of the cats walking using the my_pets instance
my_pets.walk()


# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.

    def bark(self):
        print(f'{self.name} barks')
# run_speed: returns the dogs running speed (weight/age *10).

    def run_speed(self):
        return (self.weight/(self.age * 10))

# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
    def fight(self, other_dog):
        self_skill = self.run_speed()*self.weight
        other_dog_skill = other_dog.run_speed()*other_dog.weight
        if self_skill > other_dog_skill:
            print(f'{self.name} won the fight')
        else:
            print(f'{other_dog.name} won the fight')

    def __str__(self):
        return self.name
# Create 3 dogs and use some of your methods


dog1 = Dog("Buddy", 5, 25)
print(dog1)
dog2 = Dog("Snoopy", 8, 15)
dog3 = Dog("Diablo", 4, 2)  # He's a chihuahua... he's screwed.

dog1.fight(dog3)
dog2.bark()
print(dog3.run_speed())

# Exercise 3 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} barks')

    def run_speed(self):
        return (self.weight/(self.age * 10))

    def fight(self, other_dog):
        self_skill = self.run_speed()*self.weight
        other_dog_skill = other_dog.run_speed()*other_dog.weight
        if self_skill > other_dog_skill:
            print(f'{self.name} won the fight')
        else:
            print(f'{other_dog.name} won the fight')


# Create a class named PetDog that inherits from Dog.
class PetDog(Dog):
    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight

# Add the attribute trained (boolean) to the PetDog class, should always start False
# bool trained = false
# Add the following methods:

# train: prints the output of bark and switches the trained boolean to True

# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”


# Exercise 4 : Family
# Write a Family class and implement the following attributes:

# members: list of dictionaries with the keys name, age and gender (‘Male’/’Female’) and is_child.
class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, name, age, gender):
        new_child = {
            'name': name,
            'age': age,
            'gender': gender,
            'is_child': True

        }
        self.members.append(new_child)
        print("You have a new kid! Congration! *DOOOT!*")

    def is_18(self, name):

        for member_dict in self.members:  # Loop over dictionaries
            if name == member_dict["name"]:  # Check Name
                if member_dict['age'] >= 18:  # Check Age
                    return True
                else:
                    return False

        else:
            return "NO MEMBER FOUND WITH THAT NAME"


family1 = Family([
    {'name': 'Michael',
     'age': 35,
     'gender': 'Male',
     'is_child': False}, {'name': 'Sarah',
                          'age': 32,
                          'gender': 'Female',
                          'is_child': False}], "last_name")

family1.born("Dan", 0, "Male")
print(family1.is_18('Michael'))

print(family1.members)





# last_name (string)
# Initial members data:
# [ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]
# Implement the following methods:

# born: adds a child to the members list (look up **kwargs), don’t forget to print a Congratulation message
# is_18: accept the name of one member and returns True if he is over 18, False otherwise
# a method that nicely presents the family (use the info you find relevant)


# Exercise 5 : The Incredibles Family
# Write a TheIncredibles class that inherits from the Family class:
class TheIncredibles(Family):
    def __init__(self):

        members = [
            {'name': 'Bob', 'age': 40, 'gender': 'Male', 'is_child': False,
                'power': "strength", "Alias": "Mr. Incredible"},
            {'name': 'Helen', 'age': 38, 'gender': 'Female',
                'is_child': False, 'power': "stretch", "Alias": "Elastagirl"},
            {'name': 'Violet', 'age': 18, 'gender': 'Male',
                'is_child': False, 'power': "invisibility", "Alias": "Vi"},
            {'name': 'Dash', 'age': 16, 'gender': 'Male',
                'is_child': False, 'power': "speed", "Alias": "Dash"},
        ]

        Family.__init__(self, members, "Parr")

    def use_power(self, name):
        if self.is_18(name):
            for member_dict in self.members:  # Loop over dictionaries
                if name == member_dict["name"]:  # Check Name
                    print(member_dict['power'])
        else:
            raise Exception("You have no power here!!")


    def incredible_presentation(self):
        print

# It is an Incredible Family, so they have powers, therefore the dictionaries get new keys called power and incredible_name
# implement a method use_power, that prints the power of a member only if the said member is over 18
# if the member isn’t over 18 raise an Exception (check how !!) saying (‘You have no power here !!’)
# add a incredible_presentation method to present them with their incredible names and powers
# Look up the names of The Incredibles characters on google and build the family
# (if you don’t find some information just improvise). Excluding baby jack !
# Print their normal presentation and their incredible presentation
# Use the ‘born’ method inherited from the family class to add Baby Jack with the power: “Unknown Power”
# Print both presentations again to check Baby Jack is born and that his power is showing when using the incredible representation
