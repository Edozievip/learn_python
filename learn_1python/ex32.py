the_count = [1, 2, 3, 4, 5]
the_count1 = ["one", "two", "three", "four", "five"]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this for-loop goes through a list
for number1 in (the_count1):
	for number in the_count:
		s = print(f"{number}. This is count {number1}.")

#same as above
for fruit in fruits:
	print("A fruit of type: %s" % fruit)

#Also we can go through mixed list too
#Notice we have to use %r since we don't know what's in it
for i in change:
	print("I got %s" % i)

#We can also build lists. first start with an empty one
elements = []

#Then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print("Adding %d to the list." % i)
	#Append is a function that list understands
	elements.append(i)

#now we can print them out too
for i in elements:
	print("Element was: %d" % i)
