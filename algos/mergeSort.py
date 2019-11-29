def mergeSort(vals):
	if len(vals) == 1:
		return vals
	p1 = mergeSort(vals[:len(vals)//2])
	p2 = mergeSort(vals[len(vals)//2:])
	arr = []
	while len(p1) > 0 and len(p2) > 0:
		num1 = p1.pop(0)
		num2 = p2.pop(0)
		if num1 < num2:
			arr.append(num1)
			p2.insert(0,num2)
		else:
			arr.append(num2)
			p1.insert(0,num1)
	while len(p1) > 0:
		arr.append(p1.pop(0))
	while len(p2) > 0:
		arr.append(p2.pop(0))
	return arr

	

def main():
	vals = [2,4,99,10]
	vals = mergeSort(vals)
	print(vals)


if __name__ == "__main__":
	main()