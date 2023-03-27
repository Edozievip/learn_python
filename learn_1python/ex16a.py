print("I want to open and write into my own file")

file_open = input("Enter file name: ")
filea = open(file_open, 'w')

print("I'm emptying the file...")
filea.truncate()

print("i want to write two lines in the file")
line_1 = input("line 1: ")
line_2 = input("line 2: ")

filea.write("1. %s\n2. %s" % (line_1, line_2))

filea.close()
