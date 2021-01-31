
# # Exercise 1 : Hello World
# # Print the following output in one line of code:
# # Hello world
# # Hello world
# # Hello world
# # Hello world

# for i in range(4): print("Hello World" )   
# #Use for i in range(x) to loop something a specific "(x)"" number of times



# # Exercise 2 : Some Math
# # Calculate the result of: (99^3) * 8
# print((99**3)*8) #** to use ^(powers/exponents)


# #Exercise 3 : What Is The Output ?
# #Predict the output of the following code snippets:
# print(5 < 3) #faLse
# print(3 == 3) #true
# print(3 == "3") #false
# print("3" > 3) #ERROR
# print("Hello" == "hello") #false


# # Exercise 4 : Your Computer Brand
# # Create a variable called computer_brand that contains the brand of your computer.
# computer_brand = "RAZER"
# # Insert and print the above variable in a sentence,like "I have a razer computer".
# print("I have a " + computer_brand + " computer")

# # Exercise 5: Your Information
# # Create a variable called name, and give it your name as a value (text)
# name = "Dov"
# # Create a variable called age, and give it your age as a value (number)
# age = "24"
# # Create a variable called shoe_size, and give it your shoe size as a value
# shoe_size = "45"
# # Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
# info = f"My name is {name} I am {age} years old, my shoe size is {shoe_size}"
# # Have your code print the info message.
# print(info)
# # Run your code

# # Exercise 7: Odd Or Even
# # Write a script that asks the user for a number and determines whether this number is odd or even.
# num = int(input("choose a number\n"))
# if num%2 == 0:
#     print("even")
# else:
#     print("odd")



# # Exercise 8 : What’s Your Name ?
# # Write a script that asks the user for his name and determines whether or not you have the same name, print out a funny message based on the outcome
# myname = "Heisenberg"
# name = input("SAY MY NAME!\n")
# if name == myname:
#     print("You're goddamn right!")
# else:
#     print("Nope!")

# # Exercise 9 : Tall Enough To Ride A Roller Coaster
# # Write a script that will ask the user for their height in inches, print a message if they can ride a roller coaster or not based on if they are taller than 145cm
# # Please note that the input is in inches and you’re calculating vs cm, you’ll need to convert your data accordingly

# height = int(input("How tall are you?(inches)\n"))
# height = height*2.54       #convert inches to cm
# if height > 145:
#     print("TALL BOI GO WEEEEE!!!!")
# else:
#     print("TOO SMOL TO RIDE THE THING")