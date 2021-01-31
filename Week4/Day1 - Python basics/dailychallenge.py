
# Daily Challenge : Build Up A String
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod

import random
string = input("Type a string of 10")
string = list(string)
random.shuffle(string)
string = "".join(string)
if len(string) < 10:
    print("String too short")
elif len(string) > 10:
    print("String too long")
else:
    for i in range (1,len(string)+1):
            print(string[0:i])
