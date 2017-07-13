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
	
def returnKthToLast(k):
	global nodea
	global nodeb
	global nodec
	global noded
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

	p1=nodea;
	p2=nodea;
	
	for i in range(k):
		p1=p1.next

	while(p1 != None):
		p1=p1.next
		p2=p2.next

	return p2.data	


print "-----Answer is------"
print returnKthToLast(3)
print "--- AND ACTUAL LIST WAS ---"
printList()
