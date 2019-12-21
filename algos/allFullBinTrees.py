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
	getAllLeafPaths(root.left,paths,currPath+'1')


def printTree(root):
	if root == None:
		return
	print(root.val)
	printTree(root.left)
	printTree(root.right)



dic = {}

vals = [x for x in range(4,0,-1)]
stack = []
first = TreeNode(vals.pop())
stack.append((first,'',1))
maxNodes = 7

trees = []
treepaths = set()

while stack:
	root, path, numNodes = stack.pop()
	# print("Path is %s" % path)
	# printTree(root)
	# print("\n\n")
	ps = []
	getAllLeafPaths(root,ps,'')
	tup = tuple(ps)
	print(tup)
	if tup in treepaths:
		continue
	else:
		treepaths.add(tup)
	if numNodes < maxNodes:
		for path in tup:
			leaf = getLeaf(root,path)
			leaf.left = TreeNode(0)
			leaf.right = TreeNode(1)
			stack.append((deepcopy(root),path+'0',numNodes+2))
			stack.append((deepcopy(root),path+'1',numNodes+2))
	else:
		trees.append(root)

print(len(trees))

