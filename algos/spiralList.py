def printSpiral(lists):
	checklist = []
	numItems = 0
	for row in lists:
		a = []
		for item in row:
			a.append(1)
			numItems+=1
		checklist.append(a)
	print(checklist)
	print(lists)

	dic = {"R":"D","D":"L","L":"U","U":"R"}
	direction = "R"
	currX, currY = 0,0
	buffstr = ""
	i = 0
	while i < numItems:
		if direction == "R":
			if currX >= len(lists[0]):
				currX -= 1
				currY+=1
				direction = dic[direction]
			elif checklist[currY][currX] == 0:
				currX -= 1
				currY+=1
				direction = dic[direction]
			else:
				checklist[currY][currX] = 0
				i+=1
				buffstr += str(lists[currY][currX])
				buffstr += ","
				currX += 1
		elif direction == "D":
			print(currX,currY)
			if currY >= len(lists):
				currY -= 1
				currX-=1
				direction = dic[direction]
			elif checklist[currY][currX] == 0:
				currY -= 1
				currX-=1
				direction = dic[direction]
			else:
				i+=1
				checklist[currY][currX] = 0
				buffstr += str(lists[currY][currX])
				buffstr += ","
				currY += 1
		elif direction == "L":
			if currX < 0:
				currX += 1
				currY -=1
				direction = dic[direction]
			elif checklist[currY][currX] == 0:
				currX += 1
				currY -=1
				direction = dic[direction]
			else:
				i+=1
				checklist[currY][currX] = 0
				buffstr += str(lists[currY][currX])
				buffstr += ","
				currX -= 1
		else:	#if direction == "U"
			if currY < 0:
				currY += 1
				currX += 1
				direction = dic[direction]
			elif checklist[currY][currX] == 0:
				currX += 1
				currY +=1
				direction = dic[direction]
			else:
				i+=1
				checklist[currY][currX] = 0
				buffstr += str(lists[currY][currX])
				buffstr += ","
				currY -= 1
	print(buffstr)


l = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
printSpiral(l)
l = [[1,2,3],[12,13,14],[11,16,15],[10,9,8]]
printSpiral(l)
l = [[1,2],[12,13],[11,16],[10,9]]
printSpiral(l)
l = [[1],[12],[11],[10]]
printSpiral(l)
l = [[1,2,3,4,5,6,7,8,9,10]]
printSpiral(l)

