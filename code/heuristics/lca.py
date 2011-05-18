import sys
from heuristics.rmq import RMQ

class LCA:
	def __init__(self):
		pass

	def _dfs(self, node, parent, level):
		self.E.append(node._id)
		self.L.append(level)
	
		for child in node.children:
			if parent is not None and child == parent:
				continue
			self._dfs(child, node, level + 1)
			self.E.append(node._id)
			self.L.append(level)

	def dfs(self, root):
		self._dfs(root, None, 0)

	def preprocess(self, tree):
		self.n = tree.size()
		root = tree.get_root()
		if root is None:
			print sys.stderr, "Aborting LCA preprocessing."
			return False
		self.E = []
		self.L = []
		self.dfs(root)
		assert len(self.E) == 2*self.n - 1
		assert len(self.L) == 2*self.n - 1
		self.R = {}
		for i in xrange(len(self.E)):
			if not self.R.has_key(self.E[i]):
				self.R[self.E[i]] = i
		self.rmq = RMQ()
		self.rmq.preprocess(self.L)
		return True

	def query(self, u, v):
		pos_u = self.R[u]
		pos_v = self.R[v]
		if pos_u > pos_v:
			pos_u, pos_v = pos_v, pos_u
		return self.E[self.rmq.query(pos_u, pos_v)]
