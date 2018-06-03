n = 1

for i in range(1, 101):
	n = n*i

sum = 0

for i in str(n):
	sum += int(i)

print(sum)