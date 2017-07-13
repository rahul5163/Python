import os

def binarySearch(itemToSearch, startIndex, endIndex, listOfItems):

	midIndex = startIndex + (endIndex-startIndex)/2

	if endIndex >= 1:

		if listOfItems[midIndex] == itemToSearch:
			print "Found at index midIndex"
			return midIndex	

		if listOfItems[midIndex] > itemToSearch:
			endIndex=midIndex
			return binarySearch(itemToSearch, startIndex, endIndex, listOfItems)
		else:
			startIndex=midIndex
			return binarySearch(itemToSearch, startIndex, endIndex, listOfItems)
	else:	
		return -1


testList=[1,2,3,4,5,6,7,8,9]

print binarySearch(2, 0, len(testList)-1, testList)
print binarySearch(3, 0, len(testList)-1, testList)
print binarySearch(8, 0, len(testList)-1, testList)
print binarySearch(0, 0, len(testList)-1, testList)
