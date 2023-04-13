class School:

	"""To get the total number of students in stem. """
	
	def __init__(self, uncle, aunty, pupil):
		self.uncle = uncle
		self.aunty = aunty
		self.pupil = pupil
		
	def count_them(self):
		print("We have: \n\t%d uncles\n\t%d aunties\n\t%d pupils in our school" % (self.uncle, self.aunty, self.pupil))
		
	def total(self):
		T = uncle + aunty
		print("The total number of teachers and pupils are:", T)
		

uncle = 12
aunty = 15
pupil = 180
		
		
		
school = School(uncle, aunty, pupil)
school2 = School(uncle + 10, aunty + 10, pupil +10)
school.count_them()

school2.count_them()
school.total()
