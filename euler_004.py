import time

def is_palindrome(number):
	number = str(number)
	if number == number[::-1]:
		return 0
	else:
		return 1

max_pal = 0
nums = range(100, 1000)

start = time.time()
for i in nums:
	for j in nums:
		product = i*j
		if is_palindrome(product) == 0:
			if product > max_pal:
				max_pal = product
end = time.time()
print(max_pal, end - start)

# why is stuff below wrong? because, for example: 999*200 might be a palindrome, 
# and that is what the code might return, whereas 857 * 899 might be 
# the greatest palindrome.

rev_nums = range(999, 99, -1)

def rev_calc(nums):
	for i in nums:
		print(i)
		for j in nums:
			print(j)
			product = i*j 
			if is_palindrome(product) == 0:
				return(product)

start_1 = time.time()
ans = rev_calc(rev_nums)
end_1 = time.time()

print(ans, end_1 - start_1)
