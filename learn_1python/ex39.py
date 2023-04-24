# Create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('_'* 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# Print some states
print('_'* 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the states then the cities dict
print('_'* 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('_'* 10)
for state, abbrev in states.items():
	print("%s is abbreviated \'%s\'" % (state, abbrev))

# Print every city in state
print('_'* 10)
for abbrev, city in cities.items():
	print("%s has the city \'%s\'" % (abbrev, city))

# Now do both at the same time
print('_'* 10)
for state, abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev]))

print('_'* 10)
# Safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print("Sorry, no Texas.")

# Get a city with a default value
city = cities.get('TX', 'Does not exist')
print("The city for the state 'TX' is: %s" % city)
