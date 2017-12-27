import numpy

def is_prime(n):
	for i in range(2, int(numpy.ceil(numpy.sqrt(n))) + 1):
		if n%i == 0:
			return 0
	return 1

ans = 5
for i in range(4, 2000000):
	if is_prime(i) == 1:
		ans += i

print(ans)

