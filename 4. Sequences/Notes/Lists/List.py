"""

	Operation 		Complexity 		 		Usage 				Method
	List creation 		O(n) or O(1) 		x = list(y) 	calls __init__(y)
	indexed get 		O(1) 		 		a=x[i] 			x.__getitem__(i)
	indexed set 		O(1) 		 		x[i] = a 		x.__setitem__(i,a)
	concatenate 		O(n) 		 		z=x+y 			z=x.__add__(y)
	append 		 		O(1) 		 		x.append(a) 	x.append(a)
	insert 		 		O(n) 		 		x.insert(i,e) 	x.insert(i,e))
	delete 		 		O(n) 		 		del x[i] 		x.__delitem__(i)
	equality 		 	O(n) 		 		x == y 			x.__eq__(y)
	iterate 		 	O(n) 		 		for a in x: 	x.__iter__()
	length 		 		O(1) 		 		len(x) 			x.__len__()
	membership 		 	O(n) 		 		a in x 			x.__contains__(a)
	sort 		 		O(n log n) 	 		x.sort() 		x.sort()

"""

class PyList:
	
	def __init__(self, contents=[], size=10):
		self.items = [None] * size
		self.num_items = 0
		self.size = size 

		for items in contents:
			self.append(items)


	def __getitem__(self, index):

		if index >= 0 and index < self.num_items:
			return self.items[index] 

		raise IndexError("PyList index out of range")	



	def __setitem__(self, index, items):
		if index >= 0 and index < self.num_items:
			self.items[index] = num_items

		raise IndexError("PyList assignment index out of range")



	def __add__(self, other):
		
		# create a new list
		new_list = PyList(size = self.num_items + other.num_items) 


		# add to new list items in "self" list
		for i in range(self.num_items):
			 new_list.append(self.items[i])


		# add to new list itemss in "other" list
		for i in range(other.num_items):
			new_list.append(other.items[i])


		# return new list		 
		return new_list	



	def __makeroom(self):
		new_size = self.size + (self.size // 4) + 1
		new_list = [None] * new_size

		for i in range(self.num_items):
			new_list[i] = self.items[i]

		self.items = new_list
		self.size = new_size	



	def append(self, item):

		# not enough room
		if self.num_items == self.size :
			self.__makeroom()

		# add items to list
		self.items[self.num_items] = item

		# increment num_items count
		self.num_items += 1



	def insert(self, i, e):

		# CASE 1: insert at end
		if i > self.num_items-1:
			self.append(e)
			return

		# CASE 2: insert in occupied space
		# first, check if list is full	
		if self.num_items == self.size:
			self.__makeroom()


		# from the rear, shift the elements  
		for j in range(self.num_items-1, i-1, -1):
			self.items[j+1] = self.items[j]	

		self.items[i] = e
		self.num_items += 1	



	def __delitem__(self, i):
				
		if i >= self.num_items:
			raise IndexError("PyList deletion index out of range")
		

		# shift the list back word	
		for index in range(i, self.num_items):

			# not last element in the list 
			if index != self.num_items-1:
				self.items[index] = self.items[index + 1]

			# last element in the list	
			else:
				self.items[index] = None

		self.num_items -= 1 



	def __eq__(self, other):

		# CASE 1: type check
		if type(self) != type(other):
			return False

		# CASE 2: length check
		if self.num_items != other.num_items:
			return False

		# CASE 3: elemental check
		for i in range(self.num_items):
			if self[i] != other[i]:
				return False

		return True 




	def __iter__(self):

		for i in range(self.num_items):
			yield self[i]



	def __len__(self):
		return self.numItems

a = PyList(contents=[1, 2, 3, 4])
print(a.size, a.num_items, a.items)

for i in a:
	print(i)
# a.insert(1, 12)
# print(a.size, a.num_items, a.items)
# del a[1]
# print(a.size, a.num_items, a.items)
# print(a[0])
# print(a == a)
