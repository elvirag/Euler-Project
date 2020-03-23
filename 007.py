# 10001st prime
   
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import math

def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n < 2 or n%2 == 0:
		return False
	if n < 9:
		return True
	if n%3 == 0:
		return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True    

limit=10001
count=1 #we know that 2 is prime
candidate=1
while count!= limit:
	candidate=candidate+2
	if is_prime(candidate):
		count += 1

print(candidate)