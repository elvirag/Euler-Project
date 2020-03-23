# Summation of primes
   
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import helper
import time
start_time = time.time()

sum_prime = 0
n=1
while n < 2000000:
	if helper.is_prime(n):
		sum_prime += n
	n += 1
print(sum_prime)
seconds = time.time() - start_time
print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
print("--- %s seconds ---" % (time.time() - start_time))