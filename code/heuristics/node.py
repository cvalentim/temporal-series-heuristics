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
