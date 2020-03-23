# 10001st prime
   
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import helper
import time
start_time = time.time()

limit=10001
count=1 #we know that 2 is prime
candidate=1
while count!= limit:
	candidate=candidate+2
	if helper.is_prime(candidate):
		count += 1

print(candidate)
seconds = time.time() - start_time
print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
print("--- %s seconds ---" % (time.time() - start_time))