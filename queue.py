# It is an abstract data type (interface)
# Basic operations (dequeue, enqueue)
# FIRST IN FIRST OUT
# It can be implemented with linked lists 
# Applications BFS BREADTH FIRST SEARCH


# it can used with an array or with a linked list

class Queue(object):

	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.insert(0, data)

	def dequeue(self, data):
		return self.queue.pop()

	def size(self):
		return len(self.queue)

