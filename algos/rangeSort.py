def superQuickSort(nums):
	if not nums:
		return []
	ma = max(nums)
	mi = min(nums)
	ret = []
	arr = [0 for i in range(mi,ma+1)]
	for num in nums:
		arr[num-mi] += 1
	l = ma+1-mi
	i = 0
	while i < l:
		ret.extend([i+mi for j in range(0,arr[i])])
		i+=1
	return ret

print(superQuickSort([1,1,1,1,2,1,1,1]))
