import os

class HashTableRepeat:
	def __init__(self, sizeOfTable):
		self.size=sizeOfTable
		self.slots=[None]*self.size
		self.data=[None]*self.size

	def hashFunction(self, size, key):
		return key%size

	def rehash(self, oldhash, size):
		return oldhash%size



	def get(self, key):
		startslot=self.hashFunction(len(self.slots), key)

		data=None
		stop=False
		found=False
		position=startslot
		while self.slots[position] !=None and not found and not stop:
			if self.slots[position] != key:
				position=self.rehash(position, len(self.slots))
				if position == startslot:
					stop=True
			else:
				found=True
				data=self.data[position]
		return data


	def put(self, key, data):
		hashvalue=self.hashFunction(key, len(self.slots))
		
		if self.slots[hashvalue] == None:
			self.slots[hashvalue]=key
			self.data[hashvalue]=data
		else:
			nextslot = self.rehash(hashvalue, len(self.slots))
			while self.slots[nextslot] != None and self.slots[nextslot]!= key:
				oldslot=nextslot
				nextslot=self.rehash(nextslot, len(self.slots))
				if oldslot==nextslot:
					break


			if self.slots[nextslot] == None:
				self.slots[nextslot]=key
				self.data[nextslot] = data
			else:
				self.data=data	
					



		
	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)
