f1 = 1
f2 = 1

i = 3

while True:
	fn = f1 + f2 

	if len(str(fn)) == 1000:
		print(i)
		break

	i += 1

	f1 = f2 
	f2 = fn