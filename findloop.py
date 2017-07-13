#you only have access to one node. the sol is to copy the data from next node
# and then delete the next node.
import os

global nodea
global nodeb
global nodec
global noded

global node1
global node2
global node4

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
noded.next=nodea

node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node1.next=node2
node2.next=nodec
#node3.next=node4
#node4.next=None

def printList():
	node=nodea;
	while(node!=None):
		print node.data
		node=node.next
	node=node1;
	while(node!=None):
		print node.data
		node=node.next

 
def findLoop(l1, l2):
	slow=l1
	fast=l2

	while(slow != fast):
		slow = slow.next
		fast = fast.next.next
	return slow

print "-----find loop in two lists------"
print "List1 & List 2 are"
#printList()
result=findLoop(nodea, node1)
print "-----Collision occured at------"
print result
