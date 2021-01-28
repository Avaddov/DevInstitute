## Convert the two following lists, into dictionaries.
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
## Hint: Use the zip method
# results = zip(keys, values)
# print(dict(results))

# Exercise 2 : Cinemax #2
# “Continuation of Exercise Cinemax of Week4Day2 XP”
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# age
# price = {<3 = 0, >2 & <13 = 10, >13 = 15}
family = {"rick": 64, 'beth': 33, 'morty': 5, 'summer': 8}
total = 0
# Using a for loop, the dictionary above, and the instructions, print out how much each family member will need to pay alongside their name


for name, age in family.items():
    if age < 3:
     price=0
    elif age < 13:
     price=10
    else:
     price=15

    print(name, age, price)

# After the loop print out the family’s total cost for the movies
total = total + price
print(total)
# Bonus: let the user input the names and ages instead of using the provided family variable 
# (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)

