# Ask a user for their birthdate (specify the format, for example: DD/MM/YYYY) and then:
birthday=input("What is your birthday? DD/MM/YYYY\n")  ###Ask user
year=int(birthday.split("/")[2])  ###convert to int 
age=2021-year   ###current year minus the current year to find age
candles=age%10 ###The number of candles should be the last cypher of their age, if they're 53, then add 3 candles.
cakeTop=''.ljust(candles,"i").center(11,'_')     ###align position using left justify and center
cakeBody="""      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~ """
print(cakeTop.rjust(18))
print(cakeBody)
# If they were born on a leap year, display two cakes !
if year%4==0:   #typical leap year cycle
  print(cakeTop.rjust(18))
  print(cakeBody)
