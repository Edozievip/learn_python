def add(a, b):
	print("Adding %d + %d" % (a, b))
	return a + b
	
def subtract(a, b):
	print("subtracting %d - %d" % (a, b))
	return a - b
	
def multiply(a, b):
	print("Multiplying %d * %d" % (a, b))
	return a * b
	
def divide(a, b):
	print("dividing %d / %d" % (a, b))
	return a / b
	

print("let's play with maths using functions")

chemy = add(13, 43)
bio = subtract(685, 29)
geo = multiply(32, 3)
econs = divide(36, 3)

print("chemy: %d\nbio: %d\ngeo: %d\necons: %d" % (chemy, bio, geo, econs))

print("Here is a puzzle")

total = add(chemy, subtract(bio, multiply(geo, divide(econs, 2))))

econs1 = divide(econs, 2)
geo1 = multiply(geo, econs1)
bio1 = subtract(bio, geo1)
chemy1 = add(chemy, bio1)
print("chemy1: %d\nbio1: %d\ngeo1: %d\necons1: %d" % (chemy1, bio1, geo1, econs1))

print("That becomes: ", total, "Can you do it by hand?")
