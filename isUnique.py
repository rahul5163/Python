import os


def isUniqueChar(str1):
	char_set=[None]*128
	for i in range(len(str1)):
		val=str1[i]
		print ord(val)
		if(char_set[ord(val)]):
			return False
		print ord(val)
		char_set[ord(val)]=True
	return True

check_fn=isUniqueChar('Raahul')
print check_fn
	
