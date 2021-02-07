

#make class
class Farm:

    def __init__(self, owner):
        self.owner = owner
        self.animals = {}  

    def add_animal(self, animalName, animalCount=1): 
        #get animal count from dictionary OR default to 0
        currentAnimalCount = (self.animals.get(animalName) or 0)
        #add the amount of animals being added
        self.animals[animalName] = currentAnimalCount+animalCount

    def get_info(self):
        output_string = f"{self.owner}'s Farm\n"
        for animal in self.animals:
            output_string += f"{animal}: {self.animals[animal]}\n"
        output_string += "E-I-E-I-0!"
        return output_string

#Expand The Farm
# Add a method to the Farm class called get_animal_types. 
# It should return a sorted list of all the animal types (names) that the farm has in it. For the example above, the list should be: ['cow', 'goat', 'sheep']
    def get_animal_types(self):
        return sorted(self.animals)
# Add another method to the Farm class called get_short_info. It should return a string like this: “McDonald’s farm has cows, goats and sheep.”
    def get_short_info(self):
        return f"{self.owner}'s Farm has {' and '.join((', '.join(self.get_animal_types())).rsplit(', ', 1))}."
# It should call the get_animal_types function.
# How would we make sure each of the animal names printed has a comma after it aside from the one before last (has an and after) and the last(has a period after)?.



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

# E-I-E-I-0!
