from heuristics.lca import LCA
from heuristics.tree import BinaryTree

class RMQLinear:
	def __init__(self):
		pass

	def preprocess(self, A):
		n = len(A)
		self.tree = BinaryTree() # cartesian tree
		# the preprocessing constructs a cartesian tree for the sequence
		last_at_right = self.tree.add_node(0, A[0])
		self.tree.set_root(0)
		for i in xrange(1, n):
			to_fix = self.tree.add_node(i, A[i])
			while True:
				if last_at_right is None or last_at_right < to_fix:
					break
				last_at_right = last_at_right.parent
			if last_at_right is None:
				self.tree.add_left_edge(to_fix._id, self.tree.get_root()._id)
				self.tree.set_root(to_fix._id)
			else:
				if last_at_right.right:
					self.tree.add_left_edge(to_fix._id, last_at_right.right._id)
				self.tree.add_right_edge(last_at_right._id, to_fix._id)
			last_at_right = to_fix
		self.lca = LCA()
		self.lca.preprocess(self.tree)

	def query(self, i, j):
		return self.lca.query(i, j)
