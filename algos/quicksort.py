import collections
import random

z = 0

def quicksort(arr,start,end):
	if start < end:
		mid = randomized_partition(arr,start,end) #alternatively, just use partition
		quicksort(arr,start,mid-1)
		quicksort(arr,mid+1,end)



def partition(arr, start, end):
	global z
	pivot = arr[end]
	i = start
	for j in range(start, end):
		if arr[j] <= pivot:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			i+=1
			z+=1
	z+=1
	temp = arr[i]
	arr[i] = arr[end]
	arr[end] = temp
	return i

def randomized_partition(arr, start, end):
	r = random.randint(start,end)
	temp = arr[r]
	arr[r] = arr[end]
	arr[end] = temp
	return partition(arr,start,end)

arr = [5,4,2,1,3,6,7,2,4]
a = collections.Counter(arr)
quicksort(arr,0,len(arr)-1)
b = collections.Counter(arr)
print(arr)
# print(a==b)
# print("Num comparisons is %d" % z)

