import os

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


def printList():
	node=nodea;
	while(node!=None):
		print node.data
		node=node.next
	
def removeDuplicate():
	global nodea
	global nodeb
	global nodec
	global noded
	nodea = LinkedListNode("first")
	nodeb = LinkedListNode("second")
	nodec = LinkedListNode("second")
	noded = LinkedListNode("third")
	nodea.previous=None
	nodea.next=nodeb
	nodeb.next=nodec
	nodec.next=noded
	nodeb.previous=nodea
	nodec.previous=nodeb
	noded.previous=nodec
	noded.next=None

	node=nodea;
	hashMap=set()
	previous=LinkedListNode(None)
	
	while(node!=None):
		if(node.data in hashMap):
			previous.next=node.next
		else:
			hashMap.add(node.data)
			previous=node
		node=node.next		
	

removeDuplicate()
printList()
