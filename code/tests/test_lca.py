import random
import unittest

from heuristics.lca import LCA
from heuristics.tree import Tree

class TestLCA(unittest.TestCase):
	def setUp(self):
		self.tree = Tree()
		self.lca = LCA()

	def test_one_edge(self):
		self.tree.add_edge(10, 1)
		self.assertFalse(self.lca.preprocess(self.tree), False)
		self.tree.set_root(10)
		self.assertTrue(self.lca.preprocess(self.tree), True)
		self.assertEqual(self.lca.query(1, 10), 10)
		self.assertEqual(self.lca.query(10, 1), 10)

	def test_tree_with_3_nodes(self):
		self.tree.add_edge(1, 7)
		self.tree.add_edge(1, 3)
		self.tree.set_root(1)
		self.assertTrue(self.lca.preprocess(self.tree), True)
		self.assertEqual(self.lca.query(1, 7), 1)
		self.assertEqual(self.lca.query(3, 1), 1)
		self.assertEqual(self.lca.query(3, 7), 1)

	def test_tree_with_4_nodes(self):
		self.tree.add_edge(1, 7)
		self.tree.add_edge(1, 3)
		self.tree.add_edge(3, 13)
		self.tree.set_root(1)
		self.assertEqual(self.tree.size(), 4)
		self.assertTrue(self.lca.preprocess(self.tree), True)
		self.assertEqual(self.lca.query(1, 7), 1)
		self.assertEqual(self.lca.query(3, 1), 1)
		self.assertEqual(self.lca.query(3, 7), 1)
		self.assertEqual(self.lca.query(3, 13), 3)
		self.assertEqual(self.lca.query(7, 13), 1)
		self.assertEqual(self.lca.query(1, 13), 1)

	def test_tree_with_5_nodes(self):
		self.tree.add_edge(1, 7)
		self.tree.add_edge(1, 3)
		self.tree.add_edge(3, 13)
		self.tree.add_edge(7, 16)
		self.tree.set_root(1)
		self.assertTrue(self.lca.preprocess(self.tree), True)
		self.assertEqual(self.lca.query(1, 7), 1)
		self.assertEqual(self.lca.query(3, 1), 1)
		self.assertEqual(self.lca.query(3, 7), 1)
		self.assertEqual(self.lca.query(3, 13), 3)
		self.assertEqual(self.lca.query(7, 13), 1)
		self.assertEqual(self.lca.query(1, 13), 1)
		self.assertEqual(self.lca.query(7, 16), 7)
		self.assertEqual(self.lca.query(13, 16), 1)
		self.assertEqual(self.lca.query(3, 16), 1)
		self.assertEqual(self.lca.query(1, 16), 1)

	def dfs(self, where, u, parent):
		if where._id == u:
			return (True, [u])
		for child in where.children:
			if parent is not None and child == parent:
					continue
			ans_child = self.dfs(child, u, where)
			if ans_child[0]:
				return (True, ans_child[1] + [where._id] )
		return (False, [])

	def brute_lca(self, u, v):
		root = self.tree.get_root()
		path_to_u = self.dfs(root, u, None)
		path_to_v = self.dfs(root, v, None)
		self.assertTrue(path_to_u[0])	
		self.assertTrue(path_to_v[0])
		path_to_u = path_to_u[1]
		path_to_v = set(path_to_v[1])
		for x in path_to_u:
			if x in path_to_v:
				return x

	def test_random_tree(self):
		import random
		for test in xrange(50):
			self.tree = Tree()
			n = random.randint(2, 50)
			root = random.randint(1, 10000)
			saw = [root]
			saw_set = set(saw)
			for i in xrange(n - 1):
				u = saw[random.randint(0, len(saw) - 1)]
				while True:
					v = random.randint(1, 10000)
					if v not in saw_set:
						saw_set.add(v)
						saw += [v]
						self.tree.add_edge(u, v)
						break
			self.assertEqual(self.tree.size(), n)
			self.tree.set_root(root)
			self.assertTrue(self.lca.preprocess(self.tree))
			for i in xrange(len(saw)):
				for j in xrange(i, len(saw)):
					u, v = saw[i], saw[j]
					self.assertEqual(self.brute_lca(u, v), self.lca.query(u, v))

suite = unittest.TestLoader().loadTestsFromTestCase(TestLCA)
unittest.TextTestRunner(verbosity = 2).run(suite)
