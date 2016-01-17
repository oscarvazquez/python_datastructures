# lets say you wanted to construct a tree from a sorted array it would be very unbalanced and we end up a with linked list 

# In an avl tree the difference in height of the two child trees at most is going to be 1 

# another solution would be red black tree

# AVL trees are faster than red black trees but require more work 

# operating systems rely heavily on this sort of data structure

# If we maintain the height of the left and right childs of the root node less than one, search should run at o(log n)

# fix the avl property from insertion upward after every insertion

# there may be several violations from insertion upwards 


# To fix the tree, were going to use something called rotations and to do this its going to be o(1)


# You are going to have 4 types of rotations

# 	LL: double left heavy situation: we have to make a right rotation
# 	LR: we have to make a left and a right rotation 
# 	RL: We have to make a left and a right rotation
# 	RR: we have to make a left rotation 

class Node(object):

	def __init__(self, data, parentNode):
		self.data = data
		self.parentNode = parentNode
		self.rightChild = None
		self.leftChild = None
		self.balance = 0

	def insert(self, data, parentNode):

		if data < self.data:
			if not self.leftChild:
				self.leftChild = Node(data, parentNode)

			else:
				self.leftChild.insert(data, parentNode)

		else:
			if not self.rightChild:
				self.rightChild = Node(data, parentNode)

			else: 
				self.rightChild.insert(data, parentNode)

		return parentNode

	def traverseInOrder(self):
		if self.leftChild:
			self.leftChild.traverseInOrder()

		print self.data

		if self.rightChild:
			self.rightChild.traverseInOrder()

	def getMax(self):
		if not self.rightChild:
			return self.data

		else: 
			return self.rightChild.getMax()

	def getMin(self):
		if not self.leftChild:
			return self.data

		else: 
			return self.rightChild.getMin()


class balancedTree(object):
	def __init__(self):
		self.rootNode = None

	def insert(self, data):
		parentNode = self.rootNode

		if self.rootNode == None:
			parentNode = Node(data, None)
			self.rootNode = parentNode

		else: 
			parentNode = self.rootNode.insert(data, self.rootNode)

		self.rebalanceTree(parentNode)

	def rebalanceTree(self, parentNode):

		self.setBalance(parentNode)

		if parentNode.balance < -1:
			if self.height(parentNode.leftChild.leftChild) >= self.height(parentNode.leftChild.rightChild):
				parentNode = self.rotateRight(parentNode)
			else: 
				parentNode = self.rotateLeftRight(parentNode)
		elif parentNode.balance > 1:
			if self.height(parentNode.rightChild.rightChild) >= self.height(parentNode.rightChild.leftChild):
				parentNode = self.rotateLeft(parentNode)

			else:
				parentNode = self.rotateRightLeft(parentNode)

		if parentNode.parentNode is not None:
			self.rebalanceTree(parentNode.parentNode)
		else:
			self.rootNode = parentNode

	def rotateLeftRight(self, node):
		print "Rotation left right"

		node.leftChild = self.rotateLeft(node.leftChild)

		return self.rotateRight(node)

	def rotateRightLeft(self, node):
		print 'rotation right left'
		node.rightChild = self.rotateRight(node.rightChild)
		return self.rotateLeft(node)

	def rotateLeft(self, node):

		print 'rotating left '

		b = node.rightChild
		b.parentNode = node.parentNode

		node.rightChild = b.leftChild

		if node.rightChild is not None:
			node.rightChild.parentNode = node


		b.leftChild = node
		node.parentNode = b

		if b.parentNode is not None:
			if b.parentNode.rightChild == node:
				b.parentNode.rightChild = b
			else:
				b.parentNode.leftChild = b

		self.setBalance(node)
		self.setBalance(b)

		return b

	def rotateRight(self, node):

		print 'rotating right'

		b = node.leftChild
		b.parentNode = node.parentNode\

		node.leftChild = b.rightChild

		if node.leftChild is not None:
			node.leftChild.parentNode = node

		b.rightChild = node
		node.parentNode = b

		if b.parentNode is not None:
			if b.parentNode.rightChild == node:
				b.parentNode.rightChild = b
			else: 
				b.parentNode.leftChild = b

		self.setBalance(node)
		self.setBalance(b)

		return b

	def traverseInOrder(self):
		self.rootNode.traverseInOrder()

	def setBalance(self, node):
		node.balance = (self.height(node.rightChild) - self.height(node.leftChild))

	def height(self, node):

		if node == None:
			return - 1

		else: 
			return 1 + max(self.height(node.leftChild) , self.height(node.rightChild))



tree = balancedTree()

# tree.insert(-22)
# tree.insert(33)
# tree.insert(0)
# tree.insert(2)
# tree.insert(-3)
# tree.insert(12)

tree.insert(5)
tree.insert(7)
tree.insert(6)

tree.traverseInOrder()






