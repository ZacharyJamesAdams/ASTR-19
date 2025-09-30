# This program will compute, print, then identify the type of:  
# 	- the sum of two floats
# 	- the difference of two ints
# 	- the product of a float and an int

def float_sum(float1, float2):
	val = float1 + float2
	print(f'({float1}) + ({float2}) = {val}')
	print(f'The type of {val} is {type(val)}')

def int_diff(int1, int2):
	val = int1 - int2
	print(f'({int1}) - ({int2}) = {val}')
	print(f'The type of {val} is {type(val)}')

def mixed_prod(int1, float1):
	val = int1 * float1
	print(f'({int1}) * ({float1}) = {val}')
	print(f'The type of {val} is {type(val)}')

def main(*args,**kwargs):
	float_sum(1.23, 3.14)
	print()
	int_diff(-211, 789)
	print()
	mixed_prod(2, 3.5)

if __name__ == '__main__':
	main()
