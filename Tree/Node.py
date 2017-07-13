#Breath First Traversal

import os

class Node:
	def __init__(self, data):
		self.data=data 
		self.left=None
		self.right=None


maxleft=maxright=None
def findMaxHeight(node):
	if node == None:
		return -1

	maxleft=findMaxHeight(node.left)
	maxright=findMaxHeight(node.right)

	return max(maxright, maxleft)+1
		

tree=Node(20)
tree1=Node(10)
tree3=Node(30)
tree4=Node(40)
tree.left=tree1
tree.right=tree3
tree1.left=None
tree1.right=None
tree3.left=None
tree3.right=tree4

print findMaxHeight(tree)
	
