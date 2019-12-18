class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def contains(root,key):
            if root == None:
                return False
            f1 = contains(root.left,key)
            f3 = (root.val == key)
            f2 = contains(root.right,key)
            return f1 or f2 or f3

        def findParent(root,node):
            if root == node:
                return None
            while root.left != node and root.right!=node:
                if root.val > node.val:
                    root = root.left
                else:
                    root = root.right
            return root

        def getMin(curr):
            while curr.left!=None:
                curr = curr.left
            return curr

        def otherCheck(currBest, curr, target):
            if curr == None:
                return currBest
            if curr.val > target:
                if currBest == None:
                    currBest = curr
                if curr.val < currBest.val:
                    currBest = curr
                return otherCheck(currBest, curr.left, target)
            else:
                return otherCheck(currBest, curr.right, target)

        def replace(oldOne, newOne,root):
            newP = findParent(root,newOne)
            if newOne == newP.left:
                newP.left = newOne.right
            else:
                newP.right = newOne.right
            oldP = findParent(root,oldOne)

            newOne.left = oldOne.left
            newOne.right = oldOne.right
            if oldP == None:
                root = newOne
            else:
                if oldP.left == oldOne:
                    oldP.left = newOne
                else:
                    oldP.right = newOne
            return root

        def getSuccessor(root,curr):
            if curr.right != None:
                return getMin(curr.right)
            else:
                return otherCheck(None,root,curr.val)

        def rem(curr, parent, key,root):
            if curr == None:
                return None
            if curr.val == key:
                if parent!=None:
                    if curr.left == None:
                        if curr == parent.left:
                            parent.left = curr.right
                        else:
                            parent.right = curr.right
                    elif curr.right == None:
                        if curr == parent.left:
                            parent.left = curr.left
                        else:
                            parent.right = curr.left
                    else: #neither are none
                        root = replace(curr,getSuccessor(root,curr),root)
                else:
                    if curr.left == None:
                        if curr.right == None:
                            return None
                        else:
                            return curr.right
                    elif curr.right == None:
                        return curr.left
                    else:
                        root = replace(curr,getSuccessor(root,root),root)
                        return root

            else:
                if key < curr.val:
                    rem(curr.left,curr,key,root)
                else:
                    rem(curr.right,curr,key,root)
            return root
        if contains(root,key):
            return rem(root,None,key,root)
        return root

def constructTree(root,val):
    if root == None:
        return TreeNode(val)
    else:
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                constructTree(root.left,val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                constructTree(root.right,val)
    return root

def printTree(root):
    if root == None:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)






arr = [5]
i = 0
r = None
while i < len(arr):
    r = constructTree(r,arr[i])
    i+=1
printTree(r)
print("\n\n")


a = Solution()
r = a.deleteNode(r,5)
printTree(r)




