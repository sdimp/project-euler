def collatz(n):
	length = 1

	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		length += 1
	return length

longest = 1
best_num = 1

for i in range(1, 1000001):
	if collatz(i) > longest:
		best_num = i
		longest = collatz(i)

print(longest) 
