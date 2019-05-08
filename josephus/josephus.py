from knights import *
import matplotlib.pyplot as plt
import numpy as np
import math

#Requires num be an integer >= 1
#Returns 1 if num is a power of two, 0 otherwise
def powerOfTwo(num):
	counter = 1
	while counter < num:
		if num%counter != 0:
			return 0
		counter*=2
	return 1

#requires num be an integer >= 1
def largestPowerOfTwo(num):
	counter = 1
	while counter < num:
		counter*=2
	if counter == num:
		return counter
	else:
		return counter//2

def scale(logs, ys):
	scaleFactor = max(ys)
	for i in range(0, len(logs)):
		logs[i]*=scaleFactor

xs = []
ys = []
ls = []
logs = []



for i in range(1,9999):
	circle = Knights(i)

	while circle.status() == False:
		circle.kill()

	xs.append(i)
	ys.append(circle.getWinner())
	logs.append(powerOfTwo(i))
	ls.append(i-largestPowerOfTwo(i))
	print(xs[i-1],ys[i-1])

#scales binary ouput to graph
scale(logs,ys)

#plots josephus solution
plt.plot(xs,ys)

#plots binary output for whether or not x is a power of two
plt.plot(xs,logs)

#plots absolute difference between number of knights and max smallest power of two
plt.plot(xs,ls)


plt.show()
