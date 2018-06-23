def is_increasing(n):
	n = str(n)
	l = len(n)
	nn = n + n

	for i in range(0, l-1):
		if int(nn[i]) > int(nn[l+i+1]):
			return 0
	return 1

def is_decreasing(n):
	n = str(n)
	l = len(n)
	nn = n + n

	for i in range(0, l-1):
		if int(nn[i]) < int(nn[l+i+1]):
			return 0
	return 1

def is_bouncy(n):
	if is_increasing(n) == 0 and is_decreasing(n) == 0:
		return 1
	else:
		return 0

frac = 0
n = 100
count = 0

while frac < 99:
	n += 1

	if is_bouncy(n):
		count += 1

	frac = count * 100/n

print(n)