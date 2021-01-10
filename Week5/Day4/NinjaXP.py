import random
# Exercise 2 : Dungeons & Dragons
#1. For a game of Dungeons & Dragons, each player starts by generating a character they can play with. 
# This character has, among other things, six attributes/stats:
# Strength
# Dexterity
# Constitution
# Intelligence
# Wisdom
# Charisma
#2. These six abilities have scores that are determined randomly. 
# You do this by rolling four 6-sided dice and record the sum of the largest three dice. You do this six times, once for each ability.
# For example, the six throws of four dice may look like:
# 5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
# 3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
# 1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
# 2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
# 3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
# 6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.
#3. Create a class Character and a class Game for this exercise
#Roll for initiative, suckkas! -Borderlands reference
def stat_roll():
    stat = []
    for i in range(4):
        roll = random.randint(1,6)
        stat.append(roll)
    print(stat)
    stat.sort()
    print(stat)
    stat.pop(0)
    print(stat)
    return sum(stat)




class Character():
    def __init__(self, name):
        self.name = name 
        self.strength = stat_roll()
        self.dexterity = stat_roll()
        self.constitution = stat_roll()
        self.intelligence = stat_roll()
        self.wisdom = stat_roll()
        self.charisma = stat_roll()

    def __str__(self):
        return f'name: {self.name}\nstr: {self.strength}\ndex: {self.dexterity}\nconst: {self.constitution}\nintel: {self.intelligence}\nwisdom: {self.wisdom}\ncharm: {self.charisma}'




character1 = Character("Bjorn")
print(character1)

character2 = Character("Aerith")
print(character2)

#4. The point of this exercise is to generate characters for players looking to start a game quickly
# Start by asking the user how many players are playing
# Each user then creates his/her character, let them establish what the characters name and age are
# Output the characters created into the following formats:
# txt: a nicely formatted text file for the players to use
# json: a json file of all the characters and attributes
# Hint: the Character class should be in charge of creating characters, 
# the Game class should be in charge of how many times the Character gets instantiated and of exporting the data in json or txt
