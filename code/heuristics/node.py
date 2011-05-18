class Node:
	def __init__(self, value = None, _id = None, children = []):
		self.value = value
		self._id = _id
		self.children = children

	def __eq__(self, other):
		if self.value == other.value and \
				self._id == other._id and self.children == other.children:
			return True
		return False

class BinaryNode:
	def __init__(self, value = None, _id = None, left = None, right = None, parent = None):
		self.value = value
		self._id = _id
		self.left = left
		self.right = right
		self.parent = parent

	def __lt__(self, other):
		if self.value == other.value:
			return self._id < other._id
		return self.value < other.value

	def __gt__(self, other):
		if self.value == other.value:
			return self._id > other._id
		return self.value > other.value

	def __eq__(self, other):
		return self._id == other._id
	
	@property
	def children(self):
		res = []
		if self.left:
			res += [self.left]
		if self.right:
			res += [self.right]
		return res
