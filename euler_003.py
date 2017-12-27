# to find largest prime number, keep dividing by the smallest prime factor
# until you are left with only one prime number. this will by default be the 
# largest. 

import math 

n = 600851475143

def smallest_prime_factor(n):
	n_root = int(math.ceil(math.sqrt(n)))
	for i in range(2, n_root+1):		# range starting from 2, since 1 divides everything. 
		if n % i == 0:
			return i 					# will return the smallest prime factor.
	return n 							# n itself is a prime number. 


def largest_prime_factor(n):
	while True:
		i = smallest_prime_factor(n)	# find smallest prime factor, divide n by that
		div = n/i 
		if div != 1:					# if quotient is not 1, then n is not largest prime factor
			n = div
		else:
			return i

ans = largest_prime_factor(n)
print(ans)

