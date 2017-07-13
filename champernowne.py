import os

def findval(n):
	no = 1
	depth = '1'

	while(len(depth) < n):
		no = no+1
		print no
		depth = depth+str(no)
		print depth

	return depth[n-1]

print findval(578)
