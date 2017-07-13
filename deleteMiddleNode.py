#you only have access to one node. the sol is to copy the data from next node
# and then delete the next node.
import os

global nodea
global nodeb
global nodec
global noded


class LinkedListNode: 
	def __init__(self, initData):
		self.data = initData
		self.next = None
		self.previous = None

	def getData(self):
		return self.data


	def setData(self, newData):
		self.data=newData


  	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next=newNext

	def getPrevious(self):
		return self.previous

	def setPrevious(self, newPrevious):
		self.previous = newPrevious

nodea = LinkedListNode("first")
nodeb = LinkedListNode("second")
nodec = LinkedListNode("NodeC")
noded = LinkedListNode("third")
nodea.previous=None
nodea.next=nodeb
nodeb.next=nodec
nodec.next=noded
nodeb.previous=nodea
nodec.previous=nodeb
noded.previous=nodec
noded.next=None

def printList():
	node=nodea;
	while(node!=None):
		print node.data
		node=node.next
	
def deleteMiddleNode(middlenode):

	if(middlenode == None or middlenode.next==None):
		print "Invalid Node - can't be removed"
		return None

	nextNode=middlenode.next
	middlenode.data=nextNode.data
	middlenode.next=nextNode.next
	
		
print "-----deleting nodec------"
deleteMiddleNode(noded)
print "--- AND NEW LIST IS ---"
printList()
