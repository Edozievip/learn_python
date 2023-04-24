print("Welcome to DLCF Oko. Enter your details please:")
def print_three(*args):
	gender = input("Gender: ")
	name, age, weight, height = args
	
	
	
	if gender == "male":
		print(f'His name is {name}, he is {age} years old. \nHis weight and height is {weight}kg and {height}ft respectively.')
		print(f"\tWelcome Mr {name}")
	else:
		print(f'Her name is {name}, she is {age} years old. \nHer weight and height is {weight}kg and {height}ft respectively.')
		print(f"\tWelcome Mrs {name}")
	
name = input("FullName: ")
age = input("Age: ")
weight = input("Weight in kg: ")
eight = input("Height in ft: ")
print_three(name, age, weight, eight)

#def print_two(*args):
	#print(f"Welcome Mr {name}")
	#print_three(name, age, weight, eight)
	
#print_two(name, age, weight, eight)
