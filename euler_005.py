# note that for lcm and gcd lcm(a, b, c, ...) = lcm(lcm(a, b), c, ... ) 
# and so on, so doing this in the head is an option

def is_div(n):
	for i in range(1,21):
		if n%i != 0:
			return 0
	return 1 

n = 1

while True:
	if is_div(n) == 1:
		print(n)
	else:
		n += 1