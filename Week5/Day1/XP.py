# Exercise 1: Cats
# Consider this class

def oldestcat(cat_list):
    eldestcat_age = 0
    eldestcat_name = 0
    for cat in cat_list:
        if cat.age > eldestcat_age:
            eldestcat_name = cat.name
            eldestcat_age = cat.age
    print(f"The oldest cat is {eldestcat_name}, and is {eldestcat_age} years old.")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Bob", 5)
#print(cat1.name)
# Instantiate 3 Cat objects using our class
cat2 = Cat("Fluffy", 8)
#print(cat2.name)

cat3 = Cat("Mr. Bitey", 7)
#print(cat3.name)
my_cats = [cat1, cat2, cat3]
oldestcat(my_cats)
# Create a function that finds the oldest cat and returns the cat
# for cat in my_cats:
#     print(cat.name)
# Print out: “The oldest cat is , and is years old.” using the method previously created

# # Exercise 2 : Dogs
# # Create a class Dog.
# class Dog:
# # In this class, create a method __init__, that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
# # Create a method named bark that prints “ goes woof!”]
#     def bark(self):
#         return f"{self.name} goes woof"
# # Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
#     def jump(self):
#         return f"{self.name} jumps {self.height*2}cm high!"
# # Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# davids_dog = Dog("Rex", 50)
# # Print the details of his dog by calling the methods.
# print(davids_dog.bark())
# print(davids_dog.jump())
# # Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# sarahs_dog = Dog("Teacup", 20)
# # Print the details of her dog by calling the methods.
# print(sarahs_dog.bark())
# print(sarahs_dog.jump())
# # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# if davids_dog.height > sarahs_dog.height:
#     print(davids_dog.name)
# else:
#     print(sarahs_dog.name)


# Exercise 3 : Who’s The Song Producer ?

# # Define a class called Song, it will show the lyrics of a song.
# class Song:
# # Its __init__() method should have two arguments: self and lyrics(a list).
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
# # Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
#     def sing_me_a_song(self):
#         for verse in self.lyrics:
#             print(verse)
# # Create an object, for example:
# stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
# all_star= Song(["SomeBODY once told me", "The world is gonna roll me", "I ain't the sharpest tool in the shed"])
# stairway.sing_me_a_song()
# all_star.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
class Zoo:
# In this class create a method __init__ that takes one parameter: zoo_name
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, 
# only if the new_animal isn’t already in the list.
    
    def add_animal(self, *new_animals):
        for new_animal in new_animals:
            if new_animal not in self.animals:
                self.animals.append(new_animal)
        
# Create a method get_animals that prints all the of animals in the zoo.
    def get_animals(self):
        print(f"{self.name} has these animals!")
        for animals in self.animals:
            print(animals)
# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, 
# only if he was already in the list.
    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
    def sort_animals(self):
        sorted_animals = {}
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            sorted_animals[letter]=[]
            for animal in self.animals:
                if animal[0] == letter:
                    print(animal)
                    sorted_animals[letter].append(animal)
        print(sorted_animals)
                #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def sort_animals_better(self):
        sorted_animals = {}
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            sorted_animals[letter]=[]
        for animal in self.animals:
            sorted_animals[animal[0].upper()].append(animal)
        print(sorted_animals)

# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.    

sf_zoo = Zoo("San Francisco Zoo")

sf_zoo.add_animal("Monkey")

sf_zoo.add_animal("Bear", "Baboon", "Giraffe", "Penguin", "Orangutang", "Falcon", "Aligator", "Hippopotomus", "Tiger", "Lion", "Elephant", "Salmon", "Whale", "Dolphin", "Horse", "Unicorn", "Dragon", "My neighbor Jeff")

sf_zoo.sell_animals("Penguin")

sf_zoo.sort_animals_better()
# sf_zoo.get_animals()
