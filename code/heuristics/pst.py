"""
Helper class to represent a tree node.
"""
class Node:
	def __init__(self, point = None, x_split = None, y_max = None):
		self.point = point
		self.x_split = x_split
		self.y_max = y_max
		self.left = None
		self.right = None

"""
Implements a Priority Search Tree. A fast structure
that retrives a set of points with x-coordinate below a
given limit T and y-coordinate above a given limit D.

It takes O(n log n) to construct the structure for 
a set of n points and O( log n + k) to retrive the 
k points which match a (T, D) - query.
"""

class PST:
	def __init__(self):
		pass
	"""
	points: a list of tuples in format (id, (x, y))
	"""
	def _create(self, points):
		if len(points) == 0:
			return None

		if len(points) == 1:
			tree = Node(point = points[0],
						 x_split = points[0][0], y_max = points[0][1])
			return tree

		root = points[0]
		for p in points:	
			if p[1] > root[1]:
				root = p
		x_split = points[len(points)/2][0]
		S_L = []
		S_R = []
		for p in points:
			if p == root: continue
			if p[0] <= x_split:
				S_L.append(p)
			else:
				S_R.append(p)
		node = Node(point = root, x_split = x_split, y_max = root[1])
		node.left = self._create(S_L)
		node.right = self._create(S_R)
		return node
		
	"""
	Receives a list of numbers and creates a
	priority search tree for this points.
	"""
	def create(self, points):
		self.points = points
		index_points = []
		for i in xrange(len(points)):
			index_points.append((i, points[i]))
		self.tree =	self._create(index_points)
		if len(points) >= 1:
			assert self.tree is not None
		else:
			assert self.tree is None

	def is_solution(self, point, T, D):
		return point[0] <= T and point[1] >= D

	def _query(self, tree, T, D):
		if tree is None or tree.y_max < D:
			return 

		if self.is_solution(tree.point, T, D):
			self.solutions.append(tree.point)

		if tree.x_split < T:
			self._query(tree.left, T, D)
			self._query(tree.right, T, D)
		else:
			self._query(tree.left, T, D)
	"""
	Returns all points with x <= T and y >= D
	"""
	def query(self, T, D):
		self.solutions = []
		self._query(self.tree, T, D)
		return self.solutions
