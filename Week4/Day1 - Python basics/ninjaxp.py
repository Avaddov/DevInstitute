#  Exercise_1
#/ If you want to call your program, python will check if there are any executable programs in you computer.
#/ If the file is in your path, it can be executed from this place.

# Exercise_2
# alias / second or alternate name of a piece data (eg. python = py)


# #Exercise 3
# 3 <= 3 < 9 # true
# 3 == 3 == 3 # true
# bool(0) #false
# bool(5 == "5") #false (int != str)
# bool(4 == 4) == bool("4" == "4") #true
# bool(bool(None)) #false


# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10
#​
#print("x is", x) #true
# print("y is", y) #false
# print("a:", a) #5
# print("b:", b)  #10 (because the 1 is taken from false, nothing is added to b)
# 
# 
# #Execise 4
#Use python to find out how many characters are in this text using a single line of code
# (beyond the establishment of your text variable).

# my_text = 'Lorem ipsum'
# # 
# print(len(my_text)) #11 characters 
 
# #Exercise 5
##Keep asking the user to input the longest sentence they can without the character “A” in it
##Each time a user successfully sets the new longest sentence print a congratulations message
# #Exercise 5
##Keep asking the user to input the longest sentence they can without the character “A” in it
##Each time a user successfully sets the new longest sentence print a congratulations message
length = 0
while True:
    sentence = input('What is the longest sentence you know, without A?\n')

    if 'a' in sentence or 'A' in sentence:
        print('There was an A!')
    elif len(sentence)<length:
        print(f'The sentence was shorter than {length} characters')  
    else:
        length = len(sentence) # changed.
        print(f'Well done, your sentence is {length} charecters long')