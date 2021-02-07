
# Exercise 1
# Write a script that inserts an item at a defined index in a list.
list_1 = [ 1, 2, 3, 4, 5, 6, 7 ]
list_1.insert(1, 10)
print(list_1)


# # Exercise 2
# # Write a script that counts the number of spaces in a string.
a_string = "hello world"
b_string=a_string.count(" ")
print(b_string)

# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.
script = 'AaAaAaAaAa'
ucase = 0
lcase = 0
for letter in script:

    if letter.isupper():
        ucase +=1
    else:
        lcase +=1
print(lcase, ucase)


# Exercise 6
# Write a function to find the sum of an array without using the built in function:

MySum = ([1,5,4,2,6])
def sumthing(MySum):
    total = 0
    for i in MySum:
        total = total + i
    return total
total = sumthing(MySum)
print(total)