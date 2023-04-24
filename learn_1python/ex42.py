## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ??
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name
	
## ??
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		#Person has-a pet of a kind
		self.pet = None
		
## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass
	
## ??
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("satan")

## mary is-a Person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## set crouse to an instance of class Salmon()
crouse = Salmon()

## set harry to an instance of Halibut()
harry = Halibut()
