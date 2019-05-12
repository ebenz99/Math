from math import sqrt

def isPrime(num):
	catcher = 2
	if num % catcher == 0:
		return False
	while catcher <= sqrt(num):
		if num % catcher == 0:
			return False
		catcher += 1
	return True

def generate(num):
	l = []
	for i in range(0,num):
		if isPrime(i) == True:
			l.append(i)
	return l