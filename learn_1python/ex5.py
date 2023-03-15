my_name = 'Ezeh C Chris'
my_age = 27 # this is my real age
my_height = 72 # inches
my_weight = 170 # pounds
my_eyes = 'White'
my_teeth = 'White'
my_hair = 'Black'
inches_to_centimeter = my_height * 2.5
pounds_to_kg = my_weight * 0.45359237

print("let's talk about %s." % my_name)
print("He's %d inches tall." % my_height, "i.e %d centimeters tall" % inches_to_centimeter)
print("He's %d pounds heavy." % my_weight, "or %d in kilogramme" % pounds_to_kg)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
print("If I add %d, %d, %d, %d, and  %d, I get %d." % (my_age, my_height, my_weight, inches_to_centimeter, pounds_to_kg, my_age + my_height + my_weight + inches_to_centimeter + pounds_to_kg))
