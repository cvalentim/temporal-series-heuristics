import random
import unittest

from heuristics.pst import PST, Node

class TestPST(unittest.TestCase):
	def setUp(self):
		self.pst = PST()

	def test_create_empty_sequence(self):
		self.pst.create([])
		# testando se ha lixo entre pesquisas
		self.assertEqual(self.pst.tree, None)	

	def test_create_one_sequence(self):
		self.pst.create([2])
		# testando se ha lixo entre pesquisas
		self.assertEqual(self.pst.tree.point, (0, 2))	
		self.assertEqual(self.pst.tree.x_split, 0)
		self.assertEqual(self.pst.tree.y_max, 2)

	def test_create_two_sequence(self):
		self.pst.create([3, 1])
		self.assertEqual(self.pst.tree.point, (0, 3))
		self.assertEqual(self.pst.tree.x_split, 1)
		self.assertEqual(self.pst.tree.y_max, 3)
		self.assertEqual(self.pst.tree.right, None)
		self.assertEqual(self.pst.tree.left.point, (1, 1))
		self.assertEqual(self.pst.tree.left.x_split, 1)
		self.assertEqual(self.pst.tree.left.y_max, 1)

	def test_create_three_sequence(self):
		self.pst.create([1, 3, 2])
		self.assertEqual(self.pst.tree.point, (1, 3))
		self.assertEqual(self.pst.tree.x_split, 1)
		self.assertEqual(self.pst.tree.y_max, 3)

		self.assertEqual(self.pst.tree.right.point, (2, 2))
		self.assertEqual(self.pst.tree.right.x_split, 2)
		self.assertEqual(self.pst.tree.right.y_max, 2)

		self.assertEqual(self.pst.tree.left.point, (0, 1))
		self.assertEqual(self.pst.tree.left.x_split, 0)
		self.assertEqual(self.pst.tree.left.y_max, 1)

	def test_query_empty_sequence(self):
		self.pst.create([])
		self.assertEqual(self.pst.query(10, 2), [])

	def test_query_one_sequence(self):
		self.pst.create([10])
		self.assertEqual(self.pst.query(10, 1), [(0, 10)])
		self.assertEqual(self.pst.query(-1, 11), [])

	def test_query_two_sequence(self):
		self.pst.create([10, 2])
		self.assertEqual(self.pst.query(10, 1), [(0, 10), (1, 2)])
		self.assertEqual(self.pst.query(2, 5), [(0, 10)])
		self.assertEqual(self.pst.query(-1, 1), [])

	def test_query_three_sequence(self):
		self.pst.create([10, 2, 7])
		self.assertEqual(self.pst.query(10, 1), [(0, 10), (1, 2), (2, 7)])
		self.assertEqual(self.pst.query(1, 5), [(0, 10)])
		self.assertEqual(self.pst.query(3, 8), [(0, 10)])
		self.assertEqual(self.pst.query(3, 3), [(0, 10), (2, 7)])
		self.assertEqual(self.pst.query(-1, 1), [])

	def test_query_1000_sequence(self):
		self.pst.create([x for x in xrange(1, 1001)])
		self.assertEqual(len(self.pst.query(1001, 1)), 1000) 
		self.assertEqual(len(self.pst.query(1001, 2)), 999) 
		self.assertEqual(len(self.pst.query(1001, 999)), 2) 
		self.assertEqual(len(self.pst.query(1001, 1000)), 1) 
		
		self.assertEqual(len(self.pst.query(1, 1000)), 0) 
		self.assertEqual(len(self.pst.query(500, 1)), 501) 

	def test_random_sequence(self):
		import random
		for x in xrange(1, 100):
			sequence = [random.randint(1, 100) for x in xrange(100)]
			self.pst.create(sequence)
			T = random.randint(1, 102)
			D = random.randint(1, 100)
			ans = []
			for i in xrange(0, len(sequence)):	
				if i <= T and sequence[i] >= D:
					ans.append((i, sequence[i]))
			ans = sorted(ans, key =  lambda x: x[0])
			ans_pst = sorted(self.pst.query(T, D), key = lambda x: x[0])
			self.assertEqual(ans_pst, ans)
				
		

suite = unittest.TestLoader().loadTestsFromTestCase(TestPST)
unittest.TextTestRunner(verbosity = 2).run(suite)
