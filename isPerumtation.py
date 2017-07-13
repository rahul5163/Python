import os

def sortString(s):
	new=''.join(sorted(s))
	print new
	return new

def isPermutation(s, t):
	if len(s) != len(t):
		return False

	if sortString(s) != sortString(t):
		return False
	return True


check_fn= isPermutation('Rahul Srivastava', 'Rahul Srivastava')
print check_fn
	
	
