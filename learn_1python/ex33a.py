"""Defines a whie_loop function on while and for loop"""

def while_loop(a, b):
	"""This appends a number to a list, increments and finally prints out the whole numberwhen the function is called"""
	i = 1
	while i < b:
		print(f"At the top i is {i}")
		number.append(i)
	
		i += 1
		print(f"The number is {number}")
		print(f"At bottom i is {i}")

	print()
	print("The numbers are:")
	for num in number:
		print(num)
	
number = []	
while_loop(0, 3)
print("\n")


"""Below is a multiplication table by 2."""
c = 2

while c < 12:
	for nu in range(1, 13):
		print(f"{c} * {nu:2} = {c * nu:3}")
	break
print("\n")
	
v = 2
c = int(input()) * v
#
print(f" {v} * {c} = {v * c}")
