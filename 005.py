# Smallest multiple

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time

start_time = time.time()

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i * j) % k == 0:
                i *= j
                break
print(i)
seconds = time.time() - start_time
print('Time Taken:', time.strftime("%H:%M:%S", time.gmtime(seconds)))
print("--- %s seconds ---" % (time.time() - start_time))
