"""If Statement"""

people = 20
cats = 30
dogs = 15


if people < cats:
	print("Too many cats! The world is doomed!")
	
if people > cats:
	print("Not many cats! The world is saved.")
	
if people < dogs:
	print("The world is drolled on!")
	
if people > dogs:
	print("The world is dry!")
	
	
dogs += 5

if people >= dogs:
	print("People are greater or equal to dogs.")
	
if people <= dogs:
	print("People are less or equal to dogs.")


if people == dogs:
	print("People are dogs.")
	
#The if statement runs the code under it if the boolean expression is True.
