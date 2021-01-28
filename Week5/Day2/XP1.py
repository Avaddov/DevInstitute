# Exercise 1 : Pets
# Consider this code

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

#         # Add another cat breed

# class Sphynx(Cat):
#     def walk(self):
#         return f'{self.name} is doing cat things'

# # Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# cat1 = Bengal("Mizuki", 7)
# cat2 = Chartreux("Fluffy", 4)
# cat3 = Sphynx("Beerus", 10)
# my_cats = [cat1, cat2, cat3]
# # Instantiate the Pet class with all your cats. Use the variable my_pets
# my_pets = Pets(my_cats)
# # Output all of the cats walking using the my_pets instance
# my_pets.walk()


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
        return (self.weight/(self.age *10))
        
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
    def fight(self, other_dog):
        self_skill = self.run_speed()*self.weight
        other_dog_skill = other_dog.run_speed()*other_dog.weight
        if self_skill>other_dog_skill:
            print(f'{self.name} won the fight')
        else: 
            print(f'{other_dog.name} won the fight')
            
    def  __str__(self):
        return self.name 
# Create 3 dogs and use some of your methods

dog1 = Dog("Buddy", 5, 25)
print(dog1)
dog2 = Dog("Snoopy", 8, 15)
dog3 = Dog("Diablo", 4, 2) #He's a chihuahua... he's screwed. 

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
        return (self.weight/(self.age *10))

    def fight(self, other_dog):
        self_skill = self.run_speed()*self.weight
        other_dog_skill = other_dog.run_speed()*other_dog.weight
        if self_skill>other_dog_skill:
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
#bool trained = false
# Add the following methods:

# train: prints the output of bark and switches the trained boolean to True

# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”