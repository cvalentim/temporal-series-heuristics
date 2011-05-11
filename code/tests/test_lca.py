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









suite = unittest.TestLoader().loadTestsFromTestCase(TestLCA)
unittest.TextTestRunner(verbosity = 2).run(suite)
