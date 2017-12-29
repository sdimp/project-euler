# first note that we only have to check up to 6 digit numbers, 
# this is because 9^5 = 59049, and 59059*7 is a 6 digit number. 
# knowing this, we can simply brute force, as 10^7 numbers 
# should be pretty quick on today's computers. 

def five_sum(n):
	return(sum([int(i)**5 for i in str(n)]))

s = 0
for i in range(2, 1000000):
	if i == five_sum(i):
		print(i)
		s += i

print(s)