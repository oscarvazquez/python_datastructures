class node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None;

	def remove(self, data, previousNode):
		if self.data == data:
			previousNode.next = self.nextNode
			del self.data
			del self.nextNode
		else: 
			if self.nextNode is not None:
				self.nextNode.remove(data, self)
			else: 
				print 'that node does not exist'


class linkedList(object):

	def __init__(self):
		self.head = None
		self.counter = 0

	def traverseList(self):

		actualNode = self.head

		while actualNode is not None:
			print actualNode.data
			actualNode = actualNode.nextNode

	def insertStart(self, data):
		self.counter += 1

		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else: 
			newNode.nextNode = self.head
			self.head = newNode

	def size(self):
		return self.counter

	def insertEnd(self, data):

		if not self.head: 
			self.insertStart(data)
			return

		self.counter += 1

		newNode = Node(data)

		actualNode = self.head

		while actualNode.nextNode is not None:

			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode




