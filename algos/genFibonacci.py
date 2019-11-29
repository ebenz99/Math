import math

def getFib(i):
	gp = (1+math.sqrt(5))/2
	gn = (1-math.sqrt(5))/2
	ret = ((gp**i) - (gn**i))/math.sqrt(5)
	return ret



def main():
	print(int(getFib(12)))


if __name__ == "__main__":
	main()