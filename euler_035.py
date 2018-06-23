import sympy

def is_circ_prime(n):
	numnum = str(n) + str(n)
	length = len(str(n))

	for i in range(0, length):
		if sympy.isprime(int(numnum[i:i+length])) == 0:
			return 0

	return 1

count = 0

for i in range(1000001):
	if is_circ_prime(i) == 1:
		count += 1

print(count)