class Rect(object):
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		
	def widht(self):
		x = self.width * self.height + 40
		print(x)
		print("the width is ", self.width)
		
	def heigth(self):
		print("the height is ", self.height)
		
	def arae(self):
		
		print("The Area is ", self.width * self.height)
	
#rec = Rect(9, 5)


#rec.height = 15
#rec.widht()
#rec.heigth()
#rec.arae() 

class Person(object):

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
	
	def printname(self):
		print(self.firstname, self.lastname)

class Student(Person):

	def __init__(self, fname, lname, year, englishscore):
		Person.__init__(self, lname, fname)
		self.graduationyear = year
		self.englishscore = englishscore
		
	def studentdata(self):
		print(self.firstname, self.lastname, "scored", self.englishscore, 
		"in English and graduated in", self.graduationyear)
		

st = Student("Edozie", "Christian", 2015 + 6, 84)
xt = Person("Ezeh", "Collins")
xt.printname()
st.studentdata()
#st.graduationyear = 2015 + 5
#print(st.graduationyear)


x = Person("Ezeh", "Leonard")
#x.printname()
