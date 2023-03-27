# names, variables, code and functions
def print_two(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" % (arg1, arg2))
	
# Another method to do the above
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))
	
# function with one arguement
def print_one(arg1):
	print("arg1: %r" % arg1)
	
# function with zero arguement
def print_none():
	print("Print nothing")
	
print_two("first", "second")
print_two_again("first1", "second2")
print_one("only one")
print_none()
