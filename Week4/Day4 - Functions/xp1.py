# Exercise 1 : What Are You Learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

# def display_message():

#     print("I am learning functions")

# display_message()


# Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.

# def fav_book(title):
#     print("One of my favorite books is " + title)

# fav_book("Mistborn")

# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# def city_info(City="Tokyo", Country="Japan"):
#     print(City + " is in " + Country)
# city_info("New York", "USA")
# city_info("Paris", "France")
# city_info("Jerusalem", "Israel")
# city_info()

# #Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message to the user, otherwise show a fail message and display both numbers


# def 

# Exercise 5 : Let’s Create Some Personalized Shirts !
## Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
## The function should print a sentence summarizing the size of the shirt and the message printed on it.
# def make_shirt(size="L", text="I love Python"):
#     print("Shirt Size: " + size + "\nStyle: " + text)
# # Call the function once using positional arguments to make a shirt.
# make_shirt("L", "I'm a parselmouth, I speak Python.")
# # Call the function a second time using keyword arguments.
# make_shirt(text="I love Python", size="XL")
# # Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.(Line 43)
# # Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# make_shirt()
# make_shirt("M")
# make_shirt("S", "I love Pokemon")


# Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
magicians = ["Harry", "David", "Criss"]
def show_magicians(magician_list):
  for name in magician_list:
    print(name)
show_magicians(magicians)
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.
def make_great(magician_list):
  for name in magician_list:
    name = name + " The Great"
make_great(magicians)
show_magicians(magicians)
