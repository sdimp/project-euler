# brute force solution

import numpy as np

count = 0

def comp_fac(n, r):
	return np.math.factorial(n)/( np.math.factorial(r) * np.math.factorial(n - r) )

for n in range(1, 101):
	for r in range(n+1):
		if comp_fac(n, r) > 1000000:
			count += 1

print(count)

