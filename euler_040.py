string = '0'
i = 1

while len(string) < 1000001:
	string += str(i)
	i += 1

print(int(string[1])*int(string[10])*int(string[100])*int(string[1000])*int(string[10000])*int(string[100000])*int(string[1000000]) )