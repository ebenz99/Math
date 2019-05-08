#invariant: current < number of Knights
class Knights:
	#Requires num (aka number of knights) > 0
	#Returns Knights object
	def __init__(self, num):
		self.arr = []
		for i in range(0,num):
			self.arr.append(i)
		self.current = 0

	#Returns number of remaining knights
	def numRemaining(self):
		return len(self.arr)

	#Requires a valid Knights object
	#Returns true if one knight remains, false otherwise
	def status(self):
		if self.numRemaining() == 1:
			return True
		else:
			return False

	#Requires more than one knight remains
	#Removes next knight from the circle
	def kill(self):
		if self.current==self.numRemaining()-1:
			self.arr.pop(0)
			self.move()
		else:
			self.arr.pop(self.current+1)
			self.move()

	#Requires >= 1 knight remains
	#Moves position of currently surviving knight
	def move(self):
		if self.current == self.numRemaining() or self.current == self.numRemaining()-1:
			self.current = 0
		else:
			self.current += 1

	#requires one knight remains
	#returns number of that winning knight
	def getWinner(self):
		return self.arr[0]
