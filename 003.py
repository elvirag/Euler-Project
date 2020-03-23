# Largest prime factor
   
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import time
start_time = time.time()

n=600851475143
factor=2
lastFactor=1
while n>1:
	if n % factor == 0:
		lastFactor=factor
		n = n / factor
		while n % factor==0:
			n=n / factor
	factor=factor+1
print(lastFactor)
seconds = time.time() - start_time
print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
print("--- %s seconds ---" % (time.time() - start_time))