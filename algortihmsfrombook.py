############### Algorithm Prep For Interview ####################

######## Convert Decimal to binary #########

def decimal_to_binary(num):
	""" Converts decimal to binary number assuming non negative numbers"""
	# Easy to use stack since we need to store the values 
	stack = []
	if num <= 0:
		raise ExceptionError("Please Enter Postive decimal")

	while num > 0:
		stack.insert(0, str(num%2))
		num = num // 2

	return "0b"+"".join(stack)


# print decimal_to_binary(35)

####### Convert Integer to String using Recursion#######

def integer_to_string(num):
	"""Using Recursion convert int to str"""

	if num <=0 :
		raise ExceptionError("Please enter a positive integer")

	if num < 10:
		return str(num)

	return integer_to_string(num//10) + str(int(num%10))

result = integer_to_string(769)


####### Reverse string using Recursion #######

def reverse_string(string):
	""" Using recursion return new string reversed"""

	if type(string) is not str:
		raise ExceptionError("Please enter valid string")

	if string == 1:
		return string[0] 

	return string[1:]+string[0]
print reverse_string("uhom")