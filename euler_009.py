# brute force solution, should take ~ 5 secs. 

# the for loops can be optimized, since we actually only need
# b and c; a = 1000 - b - c, and this should save us a
# considerable amount of time. 

def is_triplet(a, b, c):
	if a**2 + b**2 == c**2:
		return 1
	else:
		return 0

def fun(num):
	for c in range(num):
		for b in range(c):
			for a in range(b):
				if is_triplet(a, b, c) == 1:
					if a+b+c == 1000:
						return a*b*c


print(fun(1000))

