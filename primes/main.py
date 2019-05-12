from generator import *
from math import log

l = generate(1000000)

cp = 10

cpCount = {}

cpCount[1] = 0

for num in l:
	if num/cp == 0:
		cpCount[round(log(cp,10))] += 1
	else:
		cp*=10
		cpCount[round(log(cp,10))] = 1

print(cpCount)
