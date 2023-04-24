class Song(object):

	def __init__(self):
		pass
		
	def sing_me_a_song(self, lyrics):
		self.lyrics = lyrics
		for line in (self.lyrics):
			print(line)
			
	def addition(self, length, width):
		self.le = length
		self.wi = width
		print("The area is", self.le * self.wi)

happy_bday = Song()

bulls_on_parade = Song()

happy_bday.sing_me_a_song(["Happy birthday to you",
				 		   "I don't want to get sued",
				 		   "So I will stop right there"])

bulls_on_parade.sing_me_a_song(["They rally around the family",
					   		    "with pockets full of shells"])

area = Song()

area.addition(12, 20)
