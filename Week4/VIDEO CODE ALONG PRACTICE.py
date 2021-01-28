# Python Basics: Sets


















# Python Basics : Enumerate()

# for i, char in enumerate('Hello'):
#     print(i, char)

    
# for i, char in enumerate(list(range(100))):
#     print(i, char)
#     if char == 50:
#         print(f'index of 50 is: {i}')



#counter
# my_list = [1,2,3,4,5,6,7,8,9,10]

# counter = 0
# for item in my_list:
#     counter = counter + item 
# print(counter)


# List Comprehension
#list, set, dictionary

# my_list = [char for char in 'hello']

# # for char in "hello":
# #     my_list.append(char)
# my_list2 = [num for num in range(0,100)]
# my_list3 = [num*2 for num in range(0,100)]
# my_list4 = [num**2 for num in range(0,100) if num  % 2 == 0]

# print(my_list4)
#Set And Dictionary Comprehension
##^Works with sets{}

# simple_dict = {
#     'a':1,
#     'b':2
# }
# my_dict = {key:value**2 for key,value in simple_dict.items()
# if value%2==0}

# my_dict = {num:num**2 for num in [1,2,3]}

# print(my_dict)





# OOP: Dunder Methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color}'   

    def __len__(self):
        return 5     

    def __call__(self):
        return('yes?')

    # def __del__(self):
    #     print('deleted!')
    #     

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure)
# del action_figure