"""A linear-time algorithm is one with a linear relationship between the
amount of input and the amount of work done."""


swaps = input()

ball_location =1

for swap_type in swaps:
	if swap_type == 'A' and ball_location == 1:
		ball_location == 2
	elif swap_type == 'A' and ball_location == 2:
		ball_location == 1
	elif swap_type == 'B' and ball_location == 2:
		ball_location == 3
	elif swap_type == 'B' and ball_location == 3:
		ball_location == 2
	elif swap_type == 'C' and ball_location == 1:
		ball_location == 3
	elif swap_type == 'C' and ball_location == 3:
		ball_location == 1
		
print(ball_location)
