#Exercise 1 : Favorite Numbers
# // Create a set called my_fav_numbers with your favorites numbers.
# // Add two new numbers to it.
# // Remove the last one.
# // Create a set called friend_fav_numbers with your friend’s favorites numbers.
# // Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# fav_num= {"6", "666", "42"}
# fav_num.add("69")
# fav_num.add("10")
# fav_num.remove("10")

# friend_fav_num={"64", "12", "7"}
# numbers=set(fav_num)
# numbers.update(friend_fav_num)
# print(numbers)


# Exercise 2: Tuple
# Given a tuple with integers is it possible to add more integers to the tuple?
#A: No, because tuples are immutable. 

# Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive.
# num=0
# for i in range(20): num=num+1
# print(i)for i in range(20): print(i+1)

# # for i in range(20): print(i+1)


#Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
#A: Floats are numbers with decimal points (example: 8.9). Integers are solid numbers and will always slice off decimals (example: 8.9 = 8).
# Can you think of another way of generating a sequence of floats?

# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.
# list=[]
# for num in range(3, 11): ##Loop the number range
#     ##print(num/2) #Split the numbers in half.
# list.append(num/2) ##ADD TO LIST
# print(list) ##Result



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

# Exercise 7
# Given a list, use a while loop to print out every element which has an even index.
# list_thing = ["potato", "mayo", "hummus", "cereal", "toilet paper"]
# i = 0 
# while i < len(list_thing):
#     if i % 2 == 0:
#         print(list_thing[i])
#     i = i+1

        
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






# Exercise 12: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.


# def price_calc(agelist):
#     total = 0
#     for age in agelist:
#         if age < 3:
#             price=0 
#         elif age < 13:
#             price=10
#         else:
#             price=15
#         total += price 
#     print(f"total price is ${total}")

# def check_age(agelist):
#     allowed = []
#     for age in agelist:
#         if age > 15 and age < 22:
#             allowed.append(age)
#         else:
#             print(f"age {age} is not allowed to see this movie")
#     return allowed 

# order = []
# ticketbuy = input("How old is the viewer?\n")
# while ticketbuy != "quit":
#     order.append(int(ticketbuy))
#     print(f"Added {ticketbuy} to your order")
#     ticketbuy = input("Anyone else?\n")
# price_calc(check_age(order))




# Exercise 13 : Who Is Under 16?
# This time you have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.
# users = ["Bob", "Egg", "Bert"]
# valid_users = []
# for name in users:
#     age = int(input(f"How old are you, {name}?\n"))
#     if age >= 16:
#         valid_users.append(name)
# print(valid_users)



# Exercise 14: Family Members
# Using a while loop keep asking a user for input, these inputs will be used to control a menu
# On the menu we will have 4 options:
family_members = []
menuchoice = input("What would you like to do?\n Add, Remove, View, Exit\n")
while menuchoice != "Exit":
    # Add a name
    if menuchoice == "Add":
# If the user selects this ask for the name to add
        name = input("A man needs a name.\n") 
        family_members.append(name)
# Remove an existing name
    elif menuchoice == "Remove":
# If the user selects this ask for the name to remove
        name = input("A man needs a name.\n") 
        family_members.remove(name)
# View family members
    elif menuchoice == "View": 
# Print a nice list of the family members names
        print(family_members)
# Exit
    else:
        print("INVALID CHOICE")
    menuchoice = input("What would like to do?\n Add, Remove, View, Exit\n")