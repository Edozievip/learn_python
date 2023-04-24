line_number = 0
with open("names.txt") as a:
	for a_l in a:
		line_number += 1
		print("{:4} {}".format(line_number, a_l.rstrip()))
