def is_reversible(n):
	rev_n = int(str(n)[::-1])
	sum_num = n + rev_n

	for i in str(sum_num):
		if int(i) % 2 == 0:
			return 0

	return 1

count = 0

for i in range(1000000000):
	if is_reversible(i):
		count += 1

print(count)