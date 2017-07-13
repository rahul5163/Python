import os

class HashTable:
	def __init__(self, sizeOfTable):
		self.size=sizeOfTable
		self.slots=[None]*self.size
		self.data=[None]*self.size
	
	def hashFunction(self, key, size):
		return key%size

	def rehash(self, oldhash, size):
		return oldhash%size

	def put(self, key, data):
		hashvalue=self.hashFunction(key, len(self.slots))
	
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data
			else:
				nextslot=self.rehash(hashvalue, len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					oldslot=nextslot
					nextslot=self.rehash(nextslot,	len(self.slots))
					if oldslot == nextslot:
						break
				
				
 
				if self.slots[nextslot] == None:
					self.slots[nextslot]=key	
					self.data[nextslot]=data
				else: 
					self.data[nextslot]=data
	

	def get(self, key):
		startslot=self.hashFunction(key, len(self.slots))

		data=None
		stop=False
		found=False
		position=startslot
		while self.slots[position] !=None and not found and not stop:
			if self.slots[position] == key:
				found=True
				data=self.data[position]
			else:
				position=self.rehash(position, len(self.slots))
				if position==startslot:
					stop=True
		return data	
		
	def __getitem__(self, key):
	 	return self.get(key)

	def __setitem__(self,key, data):
		return self.put(key, data)			


