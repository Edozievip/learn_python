#!/usr/bin/python3
"""Creating a rectangle class"""


class Rectangle:
	"""This is a description of the rectangle class"""
	
	def __init__(self, width='0', height='0'):
		"""setting the rectangle class.
		Args:
			width (int): This contains the width of the rectangle.
			height (int): This contains the height of the rectangle.
		"""
		self.__width = width
		self.__height = height
		
	@property
	def width(self):
		"""This retrieves or gets the rectangles width"""
		return self.__width
	
	@width.setter
	def width(self, value):
		"""Setting the width's value"""
		if not isinstance(value, int):
			raise TypeError ("width must be an integer")
		if value < 0:
			raise ValueError ("width must be >= o")
			self.__width = value
		self.__width = 60
		print(self.__print)
		
	@property
	def height(self):
		"""This retrieves or gets the rectangles height"""
		return self.__height
	
	@height.setter
	def height(self, value):
		"""Setting the height's value"""
		if not isinstance(value, int):
			raise TypeError ("height must be an integer")
		if value < 0:
			raise ValueError ("height must be >= o")
			self.__height = value
		
		
	def area(self):
		"""This calculates the Area of the Rectangle"""
		return (self.__width * self.__height)
		
	def perimeter(self):
		"""This returns the perimeter of the rectangle"""
		if self.__width == 0 or self.__height == 0:
			return (0)
		else:
			return ((self.__width * 2) + (self.__height * 2))

R = Rectangle(20, 40)
print(R.area())
print(R.perimeter())
#R.height(50)
#print(height)
