"""Constant-Time-Algorithm - The most desirable algorithms are those that don’t do more work as the amount of input increases. No matter the problem instance, such an algorithm takes about the same number of steps. In big-O notation, we say that a constant-time algorithm is 'O(1)'."""


#our solution does the same amount of works no matter what the four digits of the phone are.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if ((num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and
		(num2 == num3)):
	print("Answer")
else:
	print("No answer")


# No how many points the Apples or Bananas have—our program 
#always does the same amount of work.
apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one

if apple_total > banana_total:
	print('A')
elif banana_total > apple_total:
	print('B')
else:
	print('T')
