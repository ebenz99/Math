# def select(arr,start,end):
# 	i = start
# 	miniMeds = []
# 	print(arr)
# 	while i+4 <= end:
# 		miniMeds.append(getMiniMedian(arr,i,i+4))
# 		i+=5
# 	if i <= end:
# 		miniMeds.append(getMiniMedian(arr,i,end))
# 	medMed = getMiniMedian()
# 	#medMed = select(miniMeds,0,len(miniMeds)-1)
# 	partition(arr,)




# def getMiniMedian(arr,start,end):
# 	for i in range(start,end+1):
# 		for j in range(i+1,end+1):
# 			if arr[j] <= arr[i]:
# 				temp = arr[i]
# 				arr[i] = arr[j]
# 				arr[j] = temp
# 	print(arr[start:end+1])
# 	return arr[start+(end-start)//2]


# def partition(arr, start, end, piv):
# 	temp = arr[piv]
# 	pivot = arr[end]
# 	i = start
# 	for j in range(start, end):
# 		if arr[j] <= pivot:
# 			temp = arr[i]
# 			arr[i] = arr[j]
# 			arr[j] = temp
# 			i+=1
# 	temp = arr[i]
# 	arr[i] = arr[end]
# 	arr[end] = temp
# 	return i

# arr = [1,2,7,4,5,5,6,7,8,12,4,3,2,1]
# print(select(arr, 0, len(arr)-1))