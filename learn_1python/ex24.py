print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\that do \n new lines and \t tabs.")

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("-" * 40)
print(poem)
print("-" * 40)


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formular(started):
	j_bean = started * 500
	jars = j_bean / 1000
	crates = jars / 100
	return j_bean, jars, crates
	
	
s_point = 10000
beans, jars, crates = secret_formular(s_point)
	
print("With a starting point of: %d" % s_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

s_point /= 10

print("We can also do that this way")
print("We'd have %d beans, %d jars, and %d crates." % secret_formular(s_point))
