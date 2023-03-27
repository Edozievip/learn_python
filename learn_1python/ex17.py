from sys import argv
from os.path import exists

fromFile = input("copying files:\n from: ")
toFile = input(" to: ")

# we could do this on one line too.
inFile = open(fromFile)
inData = inFile.read()

print("The input file is %d bytes long" % len(inData))

print("Does the output file exist? %r." % exists(toFile))
print("Ready, hit RETURN to continue. CTRL-C to abort.")
input(">> ")

outFile = open(toFile, 'w')
outFile.write(inData)

print("Alright, all done.")

outFile.close()
inFile.close()
