class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


from copy import deepcopy

# a = TreeNode(1)
# a.left = TreeNode(2)
# a.right = TreeNode(3)
# a.left.left = TreeNode(0)

# b = copy.deepcopy(a)
# b.left.left.val = 44
# print(b.left.left.val)

def getLeaf(root,path):
	leaf = root
	if path == '':
		return leaf
	for item in path:
		if item == '0':
			leaf = leaf.left
		else:
			leaf = leaf.right
	return leaf

def getAllLeafPaths(root,paths,currPath):
	if root.left == None: #and root.right==None
		paths.append(currPath)
		return
	getAllLeafPaths(root.left,paths,currPath+'0')
	getAllLeafPaths(root.right,paths,currPath+'1')


def printTree(root):
	if root == None:
		print("None")
		return
	print(root.val)
	printTree(root.left)
	printTree(root.right)

def bfsPrint(root):
	level = [root]
	items = ""
	flag = True
	while flag == True:
		flag = False
		for item in level:
			if item != None:
				flag = True
				break
		nl = []
		for thing in level:
			if thing == None:
				items += "N"
				items += ","
				continue
			items += str(thing.val)
			items += ","
			#if thing.left != None:
			nl.append(thing.left)
			#if thing.right != None:
			nl.append(thing.right)
		items+="\n"
		level = nl
	print(items)

def newPaths(paths,currPath):
	newpaths = []
	for path in paths:
		if path.startswith(currPath):
			newpaths.append(path+'0')
			newpaths.append(path+'1')
		else:
			newpaths.append(path)
	#print(newpaths)
	return tuple(newpaths)


stack = []
first = TreeNode(0)
stack.append((first,'',1,("",)))
maxNodes = 19

trees = []
treepaths = set()

while stack:
	ogroot, path, numNodes, paths = stack.pop()
	# ps = []						#nec
	# getAllLeafPaths(ogroot,ps,'')	#nec
	# tup = tuple(ps)				#nec
	tup = paths
	if tup in treepaths:
		continue
	else:
		treepaths.add(tup)
	if numNodes < maxNodes:
		for path in tup:
			root = deepcopy(ogroot)
			leaf = getLeaf(root,path)
			leaf.left = TreeNode(numNodes+1)
			leaf.right = TreeNode(numNodes+2)
			stack.append((root,path+'0',numNodes+2,newPaths(paths,path)))
			stack.append((root,path+'1',numNodes+2,newPaths(paths,path)))
	else:
		trees.append(ogroot)

#print(trees)
for tree in trees:
	bfsPrint(tree)

# null = None
# a = [[0,0,0,null,null,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0,0,0],[0,0,0,null,null,0,0,0,0,0,0],[0,0,0,null,null,0,0,0,0,0,0],[0,0,0,0,0,0,0,null,null,null,null,null,null,0,0],[0,0,0,0,0,0,0,null,null,null,null,null,null,0,0],[0,0,0,0,0,0,0,null,null,0,0],[0,0,0,0,0,0,0,null,null,0,0],[0,0,0,0,0,0,0,null,null,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
# b = [[0,0,0,null,null,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,null,null,0,0,0,0],[0,0,0,null,null,0,0,0,0,0,0],[0,0,0,null,null,0,0,0,0,null,null,null,null,0,0],[0,0,0,null,null,0,0,0,0,null,null,0,0],[0,0,0,0,0,0,0,null,null,null,null,null,null,0,0],[0,0,0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,0,0,null,null,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0,null,null,0,0],[0,0,0,0,0,null,null,null,null,0,0,0,0],[0,0,0,0,0,null,null,0,0,0,0],[0,0,0,0,0,null,null,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0,null,null,0,0]]

# #print(len(trees))
# print(len(a))
# print(len(b))

# at = []
# for item in a:
# 	at.append(tuple(item))

# bt = []
# for item in b:
# 	bt.append(tuple(item))

# aset = set(at)
# print(aset)
# bset = set(bt)

# c = aset-bset
# print(len(c))


