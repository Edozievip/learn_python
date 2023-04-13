class Robot:

	"""Represents a robot with a name. """

	# A class variable counting the number of robots
	population = 0
	animal = ("zebra", "goat")
	print(animal)

	def __init__(self, name):
		self.name = name
		print("(initializing {})".format(self.name))
	

		# when this is created, the robot adds to the population

		Robot.population += 1

	def die(self):
		"""I am dying..."""
		print("{} is being destroyed!".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print("{} was the last robot.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(Robot.population))

	def greet(self):

		"""greeting from robot"""

		print("Greetings, my master call me {}.".format(self.name))

	@classmethod
	def how_many(cls):

		"""Prints the current population."""

		print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.greet()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.greet()
Robot.how_many()

print(droid1,droid2)
print("\nRobots can do some works here.\n")

print("Robots has finished their job. let's terminate them.")
droid1.die()
droid2.die()

Robot.how_many()
