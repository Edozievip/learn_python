from sys import argv

script, userName = argv
prompt = '<< '

print("Hi %s, I'm the %s script." % (userName, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % userName)
likes = input(prompt)

print("Where do you live %s?" % userName)
lives = input(prompt)

print("What type of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
