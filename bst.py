# Bst is used to implement look up tables
# keeps the keys in sorted order, so that look up and other operations can use the principles of binaryh search

# each comparison allows the operations to skip over half the search so that each crud takes time proportional
# to the logarithm of the number of items stored in the tree

# This is much better than the linear time required to find items by key in an unsorted array, but slower than the corresponding 
# operations on a hast tables

# insertion if the key is not equal to that of the root we search the right of the subtrees recursively 

# deletion soft delete: do not actually remove the item just mark it as deleted (not so efficient )

# Deletion 

# deleting node with no child and setting it to null

# deleting a node with one child remove the node and replace it with its child

# deleting a node with two children call the node to be deleted i. Do not delete i directly. Instead choose either its in-order 
# successor node or its in order predecessor node j. Copy the value of j to i, then recursively call delete on j until reaching one of the first two cases

# In order traversal of a graph gives the numerical order 


# The height of the tree is the length of the path from the root to the deepest node in the tree, we should always try to keep the height of the tree at a minimum

# if the height of the tree is unbalanced the operations running time is no longer logarithmic

# in order traversal

class Node(object):

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

	def insert(self, data):
		if data < self.data:
			if not self.leftChild:
				 self.leftChild = Node(data)

			else:
				self.leftChild.insert(data)
		else:
			if not self.rightChild:
				self.rightChild = Node(data)
			else: 
				self.rightChild.insert(data)

	def remove(self, data, parentNode):

		if data < self.data:
			if self.leftChild is not None:
				self.leftChild.remove(data, self)

		elif data > self.data:
			if self.rightChild is not None:
				self.rightChild.remove(data, self)

		else:
			if self.leftChild is not None and self.rightChild is not None:
				self.data = self.rightChild.getMin()
				self.rightChild.remove(self.data, self)
			elif parentNode.leftChild == self:
				if self.leftChild is not None:
					tempNode = self.leftChild
				else:
					tempNode = self.rightChild

				parentNode.leftChild = tempNode

			elif parentNode.rightChild == self:
				if self.leftChild is not None:
					tempNode = self.leftChild
				else:
					tempNode = self.rightChild
				parentNode.rightChild = tempNode

	def getMin(self):
		if self.leftChild is None:
			return self.leftChild
		else:
			return self.leftChild.getMin()

	def getMax(self):
		if self.rightChild is None:
			return self.rightChild
		else: 
			return self.rightChild.getMax()

	def traverseInOrder(self):
		if self.leftChild is not None:
			self.leftChild.traverseInOrder()

		print self.data

		if self.rightChild is not None:
			self.rightChild.traverseInOrder


class BST(object):

	def __init__(self):
		self.rootNode = None

	def insert(self, data):
		if not self.rootNode:
			self.rootNode = Node(data)
		else:
			self.rootNode.insert(data)

	def remove(self, dataToRemove):
		if self.rootNode:
			if self.rootNode.data == dataToRemove:
				tempNode = Node(None)
				tempNode.leftChild = self.rootNode
				self.rootNode.remove(dataToRemove, tempNode)
				self.rootNode = tempNode.leftChild
			else:
				self.rootNode.remove(dataToRemove, None)

	def getMax(self):
		if self.rootNode:
			return self.rootNode.getMax()

	def getMin(self):
		if self.rootNode:
			return self.rootNode.getMin()

	def traverseInOrder(self):
		if self.rootNode:
			return self.rootNode.traverseInOrder()


bst = BST()

bst.insert('oscar')
bst.insert('marcos')
bst.insert('eddy')
bst.insert('gustavo')
bst.insert('azzzzz')

bst.remove('gustavo')

bst.traverseInOrder()





