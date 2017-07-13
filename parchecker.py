import os
from pythonds.basic.stack import Stack

def parChecker(inputStr):
	s=Stack()
	balanced=True
	index=0
	while index < len(inputStr) and balanced:
		symbol=inputStr[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index=index+1

	if balanced and s.isEmpty():
		return True
	else:
		return False


print parChecker("(((((())))))")
