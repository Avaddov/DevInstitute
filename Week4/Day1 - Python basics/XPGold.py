# # Exercise 1 : Hello World-I Love Python
# # Print the following output in one line of code:

# # Hello world
# # Hello world
# # Hello world
# # Hello world
# # I love python
# # I love python
# # I love python
# # I love python
# for i in range(4): print("Hello World\n"*4 + "I love Python\n"*4)


# Exercise 2 : What Is The Season ?
# Ask the user to input a month (1 to 12).
month = int(input("What month?"))
# Display the season of the month received :
# Spring runs from March (3) to May (5)
if month in [3,4,5]:
    print("Spring")
# Summer runs from June (6) to August (8)
elif month in [6,7,8]:
    print("Summer")
# Autumn runs from September (9) to November (11)

elif month in [9,10,11]:
    print("Fall")
# Winter runs from December (12) to February (2)
elif month in [1,2,12]:
    print("Winter")
else:
    print("ERROR: Not a valid month!")

notes: X in [#,#,#] = shortcut for multiple numbers in the same condition
      int(input("STRING") = Converts input into int (inputs default to string)