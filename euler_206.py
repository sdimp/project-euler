def is_okay(n):
	for i in range(0, 17, 2):
		num = (i+2)/2
		if int(str(n)[i]) != num:
			return 0
	return 1

for n in range(100000000, 150000000):
	if is_okay(n**2) == 1:
		print(n)
		break

# append a zero to the end of the number returned above!
