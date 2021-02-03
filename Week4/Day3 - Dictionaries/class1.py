inventory = {
	"apples": 100,
	"oranges": 500,
	"bananas": 200
}

# Loop through the dictionary and print:
fruitlist = inventory.items()
for fruit in fruitlist:
    print(f'I have {fruit[1]} {fruit[0]}')
# "I have <number> of <fruit>" for each line