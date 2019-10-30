class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.parent = None

def leftChild(parent,child):
	parent.left = child
	child.parent = parent

def rightChild(parent,child):
	parent.right = child
	child.parent = parent

def recTraverse(root):
	if root == None:
		return
	print(root.val)
	recTraverse(root.left)
	recTraverse(root.right)

def constTraverse(root):
	parent = 0
	left = -1
	right = 1
	frm = parent
	while True:
		if root == None:
			return

		if frm == parent:
			print(root.val)
			if root.left != None:
				root = root.left
			else:
				if root.right != None:
					root = root.right
				else:
					if root == root.parent.left:
						frm = left
					else:
						frm = right 
					root = root.parent
			continue

		elif frm == right:
			if root.parent == None:
				break
			if root == root.parent.left:
				frm = left
			else:
				frm = right 
			root = root.parent
			continue

		elif frm == left:
			if root.right != None:
				root = root.right
				frm = parent
			else:
				if root.parent == None:
					break
				else:
					if root.parent.right == root:
						frm = right
				root = root.parent
			continue

def main():
	root = TreeNode(0)
	first = TreeNode(1)
	second = TreeNode(2)
	third = TreeNode(3)
	fourth = TreeNode(4)
	fifth = TreeNode(5)
	sixth = TreeNode(6)
	seventh = TreeNode(7)	
	leftChild(root,first)
	rightChild(root,second)
	leftChild(first,third)
	rightChild(first,fourth)
	leftChild(second,fifth)
	leftChild(second,sixth)
	leftChild(third,seventh)
	constTraverse(root)

if __name__ == "__main__":
	main()