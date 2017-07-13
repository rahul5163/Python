#you only have access to one node. the sol is to copy the data from next node
# and then delete the next node.
import os

global nodea, nodeb, nodec, noded

global node1, node2, node3, node4

class LinkedListNode: 
	def __init__(self, initData):
		self.data = initData
		self.next = None

	def getData(self):
		return self.data


	def setData(self, newData):
		self.data=newData


  	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next=newNext

nodea = LinkedListNode(5)
nodeb = LinkedListNode(7)
nodec = LinkedListNode(8)
noded = LinkedListNode(3)
nodea.next=nodeb
nodeb.next=nodec
nodec.next=noded
noded.next=None

node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

def printList():
	node=nodea;
	while(node!=None):
		print node.data
		node=node.next
	node=node1;
	while(node!=None):
		print node.data
		node=node.next

 
def addTwoLists(l1, l2, carry):
	result = LinkedListNode(None)
	if(l1 == None and l2 == None and carry == 0):
		return None
	
	val=carry;	
	if(l1 !=None):
		val=val+l1.data
	if(l2 !=None):
		val=val+l2.data
	if(val >= 10 and l1 != None and l2 != None):
		carry=1
	else:
		carry=0

	result.data=val%10
	
	newList = LinkedListNode(None)
	newList=addTwoLists(l1.next, l2.next, carry)
	result.next=newList	
	return result 

print "-----adding two lists------"
print "List1 & List 2 are"
printList()
result=addTwoLists(nodea, node1, 0)
print "-----output lists------"
while(result != None):
	print result.data
	result = result.next
print "DONE!"
