def isPrime(num):
	catcher = 2
	if num % catcher == 0:
		return False
	while catcher <= num//3:
		if num % catcher == 0:
			return False
		catcher += 1
	return True


counter = 0
for i in range(0,1000):
	if isPrime(i) == True:
		print(i)
		counter += 1

print(counter)