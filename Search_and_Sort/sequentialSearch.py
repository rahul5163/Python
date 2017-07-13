import os

def sequentialSearch(itemToSearch, itemList):
	for i in range(len(itemList)):
		if itemToSearch == itemList[i]:
			print "Item found at index i"
			return True
	print "Item not found in item List	"
	return False

items=[1, 2, 3, 'two', 5, 6]

retVal=sequentialSearch('two', items)
retVal=sequentialSearch(1, items)
retVal=sequentialSearch(10, items)
retVal=sequentialSearch('three', items)

