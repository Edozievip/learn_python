x = lambda a: a + 10
print(x(100))

c = lambda a, y, z: a * y * z / 16
print(c(8, 4, 7))

def myfunc(n):
	return lambda v: v * n
double = myfunc(2)
triple = myfunc(3)

print(double(11 * 3 * 3))
print(triple(11 * 3 * 3))

import platform
import datetime

x = dir(platform)		#list all the defined names belonging to the platform module
#print(x)

x = platform.system()	#Prints the name of the operating system
print(x)

v = datetime.datetime.now()

print(v.strftime("%x"))

def famName(fname):
	print(f"{fname} Ezeh")

famName("Okey")
famName("Ikenna")
famName("Chibuike")
famName("Edozie")
