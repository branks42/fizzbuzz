# Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead 
# of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three
# and five print “FizzBuzz”.

# 1: Concatenating Strings

for num in range(1, 21):
	string = ""
	if num % 3 == 0:
		string += 'Fizz'
	if num % 5 == 0:
		string += 'Buzz'
	if num % 5 != 0 and num % 3 != 0:
		string += str(num)
	print(string)

# 2: if, elif, and else

for num in range(1, 21):
	if num % 3 == 0 and num % 5 == 0:
		print('FizzBuzz')
	elif num % 3 == 0:
		print('Fizz')
	elif num % 5 == 0:
		print('Buzz')
	else:
		print(num)
# A 3rd option
for num in range(1, 21):
	string = ''
	if num % 3 == 0:
		string = string + 'Fizz'
	if num % 5 == 0:
		string = string + 'Buzz'
	if num % 5 != 0 and num % 3 != 0:
		string = string + str(num)
	print(string, end=' ')


# END.
