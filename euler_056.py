max_sum = 0

def sum(n):
	num_sum = 0
	for i in str(n):
		num_sum += int(i)
	return num_sum

for a in range(100):
	for b in range(100):
		if max_sum < sum(a**b):
			max_sum = sum(a**b)

print(max_sum)