def heapify(arr,pos):
	l = (pos)*2+1
	r = pos*2+2
	m = pos
	if l < len(arr):
		if arr[l] > arr[m]:
			m = l
	if r < len(arr):
		if arr[r] > arr[m]:
			m = r
	if m == pos:
		return
	elif m == l:
		temp = arr[pos]
		arr[pos] = arr[l]
		arr[l] = temp
		heapify(arr,l)
		return
	elif m == r:
		temp = arr[pos]
		arr[pos] = arr[r]
		arr[r] = temp
		heapify(arr,r)
		return
	else:
		exit(1)

def build_max_heap(arr):
	for i in range(len(arr)//2,-1,-1):
		heapify(arr,i)


def heap_sort(arr):
	build_max_heap(arr)
	for i in range(len(arr)-1,-1,-1):
		temp = arr[1]
		arr[1] = arr[i]
		arr[i] = temp
		heapify(arr,i)

arr = [4,3,2,5,6]

heap_sort(arr)
print(arr)


