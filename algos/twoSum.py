def twoSum(l, target):
	s = set()
	for item in l:
		if item in s:
			return (item, target-item)
		else:
			s.add(target-item)
	return -1

print(twoSum([2,1,5,3],8))


# with open("f.ppm","rb") as f:
# 	for line in f:
# 		print(line)