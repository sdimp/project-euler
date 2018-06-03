import sympy 

i = 0
n = 0

while True:
	if sympy.isprime(n) == 1:
		i += 1

	if i == 10001:
		print(n)
		break 

	n += 1

