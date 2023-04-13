print("Welcome to savechris resturant. We have the following food varieties:\n1. swallow\n2. Rice\n3. Snacks\nChoose the number you care for:")

number = input(">> ")

if number == "1":
	print("Which type do you care for:")
	print("1. Eba with egwusi soup.")
	print("2. Eba with bitter leaf soup.")
	print("3. Eba with draw soup.")
	print("4. Eba with white soup.")
	print()
	
	Type = int(input(">> "))
	
	if Type <= 4:
		print("Your delicacy will be served in a minute.")
	else:
		print("Please choose one of the above.")
