import os

def divide(a, b):
	assert b > 0
	nmr=a//b
	rem=a%b

	visited={rem:0}
	digit=[]
	while(True):
		rem *= 10
		digit.append(rem//b)
		rem = rem % b
		if rem in visited:
			location=visited[rem]
			print "location is:" 
			print location
			return (nmr, digit[:location], digit[location:])
		else:
			visited[rem] = len(digit)
			print "visited is:" 
			print visited
			print "digit is:"
			print digit



for a, b in [(5,4), (1,6), (7,17), (2,4), (1,3)]:
	(n,f,r)=divide(a,b)
	print "%d/%d = %d.%s(%s)" % (a,b,n, ''.join(map(str,f)), ''.join(map(str,r)))
