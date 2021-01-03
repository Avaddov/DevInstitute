#VARIABLES AND VALUE TYPES:
# Predict the output of the following code snippets:
# >>> 5 < 3   FALSE
# >>> 3 == 3  TRUE 
# >>> 3 == "3" FALSE
# >>> "3" > 3  ERROR
# >>> "Hello" == "hello" FALSE 


# Exercise 2 : Some Math
# print((99**3) * 8)


# Exercise 7 : Odd Or Even
# Write a script that asks the user for a number and determines whether this number is odd or even.

# num = int(input("enter number"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Write a script that will ask the user for their height in inches, print a message if they can ride a roller coaster or not based on if they are taller than 145cm
# Please note that the input is in inches and you’re calculating vs cm, you’ll need to convert your data accordingly
# Height = int(input("How tall are you in inches?"))




#Exercise 5: Your Information
# name = "Dov"
# age = "24"
# shoesize = "45"
# info =f"my name is {name} I am {age} years old. My shoe size is {shoesize}."
# print(info)


#RANGES 
# #Use a for loop to print the numbers from 1 to 20, inclusive.

# # for i in range(21): print(i)

# # Exercise 4: Floats
# # Recap – What is a float? What is the difference between an integer and a float?
# # Can you think of another way of generating a sequence of floats?
# # Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.
# A: Floats are numbers with decimal points (example: 8.9). Integers are solid numbers and will always slice off decimals (example: 8.9 = 8).

# Exercise 5: Shopping List
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)


# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket.count("Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)



# Exercise 6 : Loop
# Write a while loop that will keep asking the user for input until the input is the same as your name.

# name = "Heisenberg"
# while input("Say my name\n") != name:
#     print("Nope.")
# else:
#     print("You're goddamn right!")

# Exercise 8
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
# l = []
# for i in range(3, 31):
#       # if equal to zero it is a multiple of 3
#     if i % 3 == 0:
#         # add it to the list
#         l.append(i)
# print(l)


# Exercise 9
# # Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.
# numbers = []
# for i in range(1500, 2700, 5):
#     if i %7 == 0:
#         numbers.append(i)
# print(numbers)

# Exercise 10: Favorite Fruits
# Ask the user to type in his/her favorite fruit(s) (one or several fruits).
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# Now that we have a list of fruits, ask the user to type in the name of any fruit.
# If the user’s input is a fruit name existing in the list above, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT a fruit name existing in the list above, print, “You chose a new fruit. I hope you enjoy it too!”.
# Bonus: Display the list in a user friendly way : add the word “and” before the last fruit in the list – but only if there are more than 1

# fruits = input("What are your favorite fruits?\n")
# fruitlist = fruits.split()
# anyfruit = input("Pick any fruit\n")
# if fruitlist.count(anyfruit) > 0:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy it too!")


# Exercise 11: Who Ordered A Pizza ?
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exit print all the toppings on the pizza and what the total is (10 + 2.5 for each topping)

# toppings = []
# order = input("What toppings do you want?\n")
# while order != "quit":
#     toppings.append(order)
#     print(f"Added {order} to your pizza")
#     order = input("What other toppings do you want?\n")

# print(toppings)
# total = (len(toppings) * 2.5) + 10
# print(total)
