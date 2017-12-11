#  File: Goldbach.py

#  Description: Returns all prime number addends that add up to the number defined in the user's range. User inputs an even lower limit 
#  greater than or equal to 4 and an upper limit that is even. Output is all the cases in the program description    

#  Student Name: Brian Tsai	

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 3/10/17

#  Date Last Modified: 3/10/17

# is_Prime returns whether a number is prime
def is_Prime(number):
	# If number is 1 then return False
	if (number == 1):
		return False		
	# The limit is the number that is the ceiling of the square root of the input
	limit = int(number ** 0.5 + 1)
	divisor = 2
	
	# Return False when it finds a number that is a factor of input other then 1 and itself
	while (divisor < limit):
		if (number % divisor == 0):
			return False
		divisor += 1
	# Return True if no other factors are found	
	return True

def main():
	# correct_input is True when the user inputs valid numbers
	correct_input = False 

	# Prompt the user until the inputs are valid: lower limit is greater or equal to 4, the upper limit is even,
	# and the upper limit is larger than the lower limit
	while (not correct_input):
		lower_limit = int(input("Enter the lower limit: "))
		upper_limit = int(input("Enter the upper limit: "))
		if (lower_limit >= 4 and lower_limit % 2 == 0 and upper_limit % 2 == 0 and (upper_limit - lower_limit > 0)): 
			correct_input = True

	# Iterate over every even number within range
	for number in range (lower_limit, upper_limit + 2, 2):
		print(number, end = " ")

		# Find all prime divisors of the number 
		for divisor in range (1, number):
			if (is_Prime(divisor) and is_Prime(number - divisor) and divisor <= number - divisor):
				print("=", divisor, "+", number - divisor, end = " ")
		print()	
main()




