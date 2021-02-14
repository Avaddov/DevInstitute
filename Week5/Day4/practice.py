import json
practiceJson = "Hello"

with open("Week5/Day4/practice.json", "w") as f:
   f.write(practiceJson) 


with open('practiceJson.json') as f:
    data = f.readlines('practiceJson.json')
    