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
