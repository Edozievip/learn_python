def add_num(a, b):
	"""Adds the two numbers and prints out the result"""
	print(a + b)
	
	if int(a + b) < 35:
		print((a + b), " is a small number.")
	else:
		print((a + b), " is a big number")
	
def sub_num(a, b):
	print(a - b)
	
def mult_num(a, b):
	print(a * b)
	
def div_num(a, b):
	print(a / b)
	
a = int(input(">>> "))
b = int(input(">>> "))

sub_num(a, b)
add_num(a, b)
#mult_num(a, b)
div_num(a, b)
