import math

def getFib(i):
	gp = (1+math.sqrt(5))/2
	gn = (1-math.sqrt(5))/2
	ret = ((gp**i) - (gn**i))/math.sqrt(5)
	return ret


def otherFib(i):
	gp = (1+math.sqrt(5))/2
	print(gp)
	print((gp**i))
	ret = ((gp**i)+(1/2))/math.sqrt(5)
	return ret


def main():
	#print(int(getFib(3)))
	print(int(otherFib(3)))
	# print((otherFib(3)))
	# print(int(getFib(199)))
	# print(int(otherFib(199)))


if __name__ == "__main__":
	main()