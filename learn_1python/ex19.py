def pea_nut(pea_count, nut_boxes):
	print("You have %d peas!" % pea_count)
	print("You have %d boxes of nuts!" % nut_boxes)
	print("Guy that's enough for a celebration!")
	print("Get a blanket.\n")
	
	
print("We can just give the function numbers directly:")
pea_nut(22, 28)


print("Or we can use variables from our script:")
amount_of_peas = 20
amount_of_nuts = 40

pea_nut(amount_of_peas, amount_of_nuts)


print("We can even do maths inside too:")
pea_nut(5 * 4, 23 + 7)


print("And we can combine the two, variables and math:")
pea_nut(amount_of_peas + (5 * 4), (amount_of_nuts * 4) - 100)
