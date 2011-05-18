import random
import unittest

from heuristics.tree import Tree
from heuristics.node import Node

class TestTree(unittest.TestCase):
	def setUp(self):
		self.tree = Tree()

	def test_add_edge(self):
		self.tree.add_edge(10, 1)
		self.assertEqual(self.tree.has_edge(1, 10), True)
		self.assertEqual(self.tree.has_edge(10, 1), True)
		self.assertEqual(self.tree.has_edge(10, 2), False)
		self.assertEqual(self.tree.has_edge(1, 15), False)
		self.assertEqual(self.tree.has_edge(2, 15), False)
		self.assertEqual(self.tree.size(), 2)

	def test_set_root(self):
		self.assertEqual(self.tree.get_root(), None)
		self.tree.add_edge(10, 1)
		self.assertEqual(self.tree.set_root(40), -1)
		self.assertEqual(self.tree.set_root(10), 10)
		self.assertNotEquals(self.tree.get_root(), None)

	def test_tree_with_3_nodes(self):
		self.tree.add_edge(1, 7)
		self.tree.add_edge(1, 3)
		self.assertTrue(self.tree.has_edge(1, 7))
		self.assertTrue(self.tree.has_edge(1, 3))
		self.assertEqual(self.tree.size(), 3)
		self.assertEqual(self.tree.set_root(1), 1)
		self.assertEqual(len(self.tree.get_root().children), 2)
		self.assertEqual(len(self.tree.get_node(7).children), 1)
		self.assertEqual(len(self.tree.get_node(3).children), 1)
		self.assertEqual(self.tree.get_node(1), self.tree.get_root())
		self.assertEqual(self.tree.get_node(17), None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTree)
unittest.TextTestRunner(verbosity = 2).run(suite)
