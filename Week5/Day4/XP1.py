# import random
# # Exercise 1 – Random Sentence Generator
# # Description: We will create a program that will generate a random sentence and display it to the user. We will allow the user to choose how long the sentence will be.

# # Hint : The random sentences do not need to make sense or to be grammatically correct

# # Download this word list

# # Save it in your development directory.

# # Create a function called get_words_from_file that will read the file’s contents and return them as a collection. What data type should you use?
# def get_words_from_file():
#    with open("Week5/Day4/sowpods.txt","r") as f:
#       list_of_words = f.readlines()
#    list_of_words = [word.strip() for word in list_of_words] 
#    return list_of_words
# # print(get_words_from_file()) #progressprint (!Do not use when running in terminal!)
# # Create another function called get_random_sentence. 
# # It should have a single parameter, length, which will be used to determine how many words the sentence should have. 
# def get_random_sentence(length):
# # The function should get the words list, and choose random words from it, according to the amount specified by length.
#    words = get_words_from_file() 
#    sentence_words = []
#    #print(sentence_words)  #progressprint 
#    for num in range(length):
#       sentence_words.append(random.choice(words)) 
#       #print(sentence_words) #progressprint
# # The words should be joined together into a string, which should be formatted in lower case (or title case) and returned.
#    sentence = " ".join(sentence_words)
#    #print(sentence) #progressprint
#    return sentence.lower()
# #print(get_random_sentence(8)) #progressprint


# # Create a main function.
# def main():
# # It should print a message explaining what the program does.
# # Ask the user how long the sentence should be. Acceptable values: an integer between 2 and 20. Validate your data, and test your validation!
#    sentence_length = input('This program will generate a "sentence" of random words based on your desired word amount. Please provide a number.\n')
#    print(sentence_length)
#    if sentence_length.isdigit():
#       sentence_length = int(sentence_length)
#       if sentence_length < 2 or sentence_length > 20:
# # If the user inputs incorrect data, print an error message and end the program.
#          print("ERROR: Please choose a number between 2 & 20. SHUTTING DOWN.")
#          exit()
#       else:
#          print(get_random_sentence(sentence_length))
#    else:
#       print("ERROR: Please choose a number between 2 & 20. SHUTTING DOWN.")
#       exit()

# main()
# If the user inputs correct data, user your functions to create a random sentence, and then display it proudly to the user.


# Exercise 2: Working With JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
# Access the nested key “salary” from the above JSON-string
test1 = json.loads(sampleJson)
print(test1["company"]["employee"]["payable"]["salary"])

# Sort the dictionary key-value pairs inside “payable” alphabetically, by their key, using code
##LMAO WUT (dictionaries aren't ordered.)

# Save the dictionary as JSON to a file
with open("Week5/Day4/XP1.json", "w") as f:
   f.write(sampleJson) 