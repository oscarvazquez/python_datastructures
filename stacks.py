# It is an abstract data type
# Basic operations pop() and push()
# Last in first OUT
# In most high level languages, a stack can be easily implemented with an array or a linked list
# A number of languages or stack oriented, they define most basic operations as taking their arguments from the stack and placing any return values back into the stack
# If an oversized data item is moved to a stack location that is not large enough to contain it return information from a procedure call may be corrupted, causing the program to fail


# buffer overflow attack

# providing oversized data input to a program that does not check the length of the input -> such program may copy the data in its
# entirety to a location in the stack, and in so doing it may change the return addresse for procedures that have called it. An attacker
#  can experiment to find a specific type of data that can be provided to such a program such that the return address of the current procedure
# is reset to the point to an area within the stack itself. (and within the data provided by the hacker) which in turn contains instructions
# that carry out unauthorized operations

# usually we can avoid using stacks by using recursion 
# BUt the os will use stack int eh background 

class stack(object):

	def __init__(self):
		self.stack = []
		self.numOfItems = 0

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.insert(self.numOfItems, data)
		self.numOfItems = self.numOfItems + 1

	def pop(self):
		self.numOfItems = self.numOfItems - 1
		dataToReturn = self.stack.pop(self.numOfItems)
		return dataToReturn

	def size(self):
		return len(self.stack)

