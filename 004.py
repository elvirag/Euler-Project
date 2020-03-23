# Largest palindrome product
   
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrom(number: int):
	str_num = str(number)
	len_num = len(str_num)
	for i in range(len_num):
		if str_num[i] != str_num[len_num -1 -i]:
			return False
	return True

def do_stuff():
	max_number = -1
	for i in reversed(range(1000)):
		for j in reversed(range(1000)):
			# print("i:", i, "j:", j)
			if isPalindrom(i*j):
				if max_number < i*j:
					max_number = i*j
	print(max_number)

do_stuff()