with open("file1", mode="w", encoding="utf-8") as b:
	b.write("I am a web developer.")
	
with open("file1", mode="a", encoding="utf-8") as b:
	b.write("\nI am also a software engineer.")
	b.write("\nI am a student of ALX.")	

with open("file1", mode="r") as b:
	print("{:<5}".format(b.read()))
	print(b.seek(0))
	print(b.readline())
	print(b.readline())
	print(b.seek(0))
	print(b.readline())
print("\n")

import gzip

z_file = gzip.open('out.log.gz', mode='w')
z_file.write('A nine mile walk is no joke, \nespecially in the rain.'.encode('utf-8'))

z_file = gzip.open('out.log.gz', mode='r')
print(z_file.read())
