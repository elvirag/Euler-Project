# Sum square difference
   
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 1^2+2^2+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)^2=552=3025
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

sum_mul = 0
sum_sqr = 0

for i in range(1,101):
	sum_mul += i
	sum_sqr += i ** 2

print(sum_mul ** 2 - sum_sqr)