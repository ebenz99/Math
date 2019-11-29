def bubbleSort(vals):
	for i in range(0,len(vals)):
		for j in range(0,len(vals)-1):
			if vals[j] > vals[j+1]:
				temp = vals[j+1]
				vals[j+1] = vals[j]
				vals[j] = temp
	return vals	

def main():
	vals = [29,2000,4,99,10,1]
	vals = bubbleSort(vals)
	print(vals)


if __name__ == "__main__":
	main()