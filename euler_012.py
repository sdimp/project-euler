# n-th triangular number is n(n+1)/2

import numpy as np 

def num_divisors(num):
	n = 0
	for i in range(1, int(np.sqrt(num))):
		if num%i == 0:
			n += 1
	n *= 2
	if num % int(np.sqrt(num)) == 0:
		n += 1
	return n 

def tri(i):
	return i*(i+1)/2

i = 1
while True:
	num = tri(i)

	if num_divisors(num) > 500:
		print(num)

	i += 1

