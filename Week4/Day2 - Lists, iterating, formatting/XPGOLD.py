# Exercise 1 : Concatenate Lists
# Write a script that concatenate two lists together without using the + sign.

# listx = [1,2,3,4,5]
# listy = [6,7,8]

# def cat(x,y):
#     result = []
#     for i in x:
#         result.append(i) 
#     for j in y:
#         result.append(j)
#     return result

# print(cat(listx, listy))

# Exercise 2: Greatest Number
# Take three numbers from the user and print the greatest number.

# num1 = input("pick a number")
# num2 = input("pick another number")
# num3 = input("pick one more number")

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)

# Exercise 3 : The Alphabet
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant

# Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for letter in Alphabet:
#     if letter in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
# 	    print("%s is a vowel." % letter)
#     else:
# 	    print("%s is a consonant." % letter) 

# Exercise 4 :
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# 1. Write a script with the list of names provided. This code should ask the user for input
# * if the input exists in the list print the index of the first occurence
# Example: if input is ‘Cortana’ we should be printing the index 1

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']  #list of characters 
# while True:   #character selection
#     character = input("Choose your character!")   
#     character_index = -1  #initialize with invalid index (-1)
#     for i in range(len(names)):   #loop over the character indeces in names array 
#         if names[i] == character and character_index == -1:   #checking if input matches characters and if the index isn't initiallized 
#             character_index = i    #return index if yes 
#     if character_index != -1:
#         print(character_index)
        
# #         Exercise 5 : Words And Letters
# # Take 7 words as input from a user and store them for use in a list named words
# # should not be done on 7 lines
# # Mad props if you can do it in one :)
# words = []
# for i in range (7): words.append(input("What's the word, bird?"))
# print(words)
# # Ask a single character input from the user and store it in a variable letter
# letter = input("pick a letter") 
# for word in words:
#     try: 
#         index = word.index(letter)
#     except ValueError:
#     # Tell the user what index letter is in each item in words
#     # If the letter doesn’t exist in a given word, print a friendly message saying so
#         print(f"the letter {letter} does not appear in the word {word}")
#     else:
#         print(f"the letter {letter} appears in the word {word} at index {index}")

# Exercise 6 :
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers .
# numbers = []
# for i in range(1000000):
#     numbers.append(i+1)
# print(min(numbers)==1)
# print(max(numbers)==1000000)
# print(sum(numbers))
# Exercise 7 :
# Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')



# Exercise 8 : Random Number
# Accept input from a user if its between 1 and 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# Print a message if the user guessed the correct number or not.
# Bonus: use a menu to let the user keep guessing until he wants to quit
# Bonus 2: on exit tally up and display total games, wins and losses


# Exercise 9: Check Please !
# Your code will print out the bill for a customer, with the help of the waiter/waitress.

# First, ask some questions, and then print out the bill.
# Store the answers to the questions in variables, so that they can be used later on in your code.
# Ask the user (waiter) for each of these pieces of information, assuming that the customer ordered only one item (but multiple orders of the same item are allowed):
# Hint: a menu like from Exercise 7 of the XP may be helpful here
# a. The customer’s name (this is a friendly bar!).
# b. The name of the waiter/waitress.
# c. The name of the item (eg. ‘beer’).
# d. The price of the item.
# e. The amount of items that were ordered (eg. 3, when the customer had 3 beers)
# f. The discount amount (user should input zero if there was no discount).
# Now calculate the total to charge the customer.
# Bonus: add VAT to the total.
# Print out a nicely formatted bill for the user, on multiple lines. Add some lines of stars or hyphens to create the effect of a “border” or “line”, to make it look more professional.
# Use at least one multi-line string in your output. Use string formatting (f-strings)