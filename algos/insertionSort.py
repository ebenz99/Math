def insertionSort(vals):
	for i in range(1,len(vals)):
		j = i - 1
		currVal = vals[i]
		while j >= 0 and currVal < vals[j]:
			vals[j+1] = vals[j]
			j -= 1
		vals[j+1] = currVal

def main():
	vals = [2,4,4,2,6,8,9,10]
	insertionSort(vals)
	print(vals)


if __name__ == "__main__":
	main()