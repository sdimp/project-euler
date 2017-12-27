# storing fibonnaci numbers is a stupid idea, they get absurly large really quickly
# so just store the sum; important lesson on space complexity here

sum = 0

x = 1
y = 2

while y <= 4000000:
	if y % 2 == 0:
		sum += y
	x, y = y, x + y 

print(sum)