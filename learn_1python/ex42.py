## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a __init__ that takes in self and name parameters
		self.name = name

## Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a __init__ that takes in self and name parameters
		self.name = name
	
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a __init__ that takes in self and name parameters
		self.name = name

		#Person has-a __init__ that takes in self and pet parameters
		self.pet = None
		
## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## super() function replaces the parent element
		## same as using Person.__init__(name) 
		super(Employee, self).__init__(name)
		## Employee has-a __init__ that takes in self and salary parameters
		self.salary = salary
		print("His name is", self.name, "and his slary is", self.salary)

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass


## rover is an instance of class Dog
rover = Dog("Rover")

## satan is an instance of class Cat
satan = Cat("satan")

## mary is an instance of class Person
mary = Person("Mary")
print(mary.name)

## from mary get the pet attribute and set it to satan
mary.pet = satan
print(satan)

## frank is an instance of class Employee
frank = Employee("Frank", 120000)
print(frank.name, frank.salary)

## from frank get the pet attribute and set it to rover
frank.pet = rover
print(rover)

## flipper is an instance of class Fish
flipper = Fish()
print(flipper)

## crouse is an instance of class Salmon
crouse = Salmon()
print(crouse)

## harry is an instance of class Halibut
harry = Halibut()
print(harry)
