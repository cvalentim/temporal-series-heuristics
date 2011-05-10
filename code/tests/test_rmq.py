import random
import unittest

from heuristics.rmq import RMQ

class TestRMQ(unittest.TestCase):
	def setUp(self):
		self.rmq = RMQ()

	def test_one_sequence(self):
		self.rmq.preprocess([2])
		# testando se ha lixo entre pesquisas
		self.assertEqual(self.rmq.query(0, 0), 2)	

	def test_two_sequence(self):
		self.rmq.preprocess([3, 1])
		self.assertEqual(self.rmq.query(0, 1), 1)
		self.assertEqual(self.rmq.query(0, 0), 3)
		self.assertEqual(self.rmq.query(1, 1), 1)

	def test_three_sequence(self):
		self.rmq.preprocess([1, 3, 2])
		self.assertEqual(self.rmq.query(0, 2), 1)
		self.assertEqual(self.rmq.query(0, 1), 1)
		self.assertEqual(self.rmq.query(1, 1), 3)
		self.assertEqual(self.rmq.query(1, 2), 2)
		self.assertEqual(self.rmq.query(2, 2), 2)

	def test_three_sequence_again(self):
		self.rmq.preprocess([10, 2, 7])
		self.assertEqual(self.rmq.query(0, 2), 2)
		self.assertEqual(self.rmq.query(0, 1), 2)
		self.assertEqual(self.rmq.query(0, 0), 10)
		self.assertEqual(self.rmq.query(1, 2), 2)
		self.assertEqual(self.rmq.query(1, 1), 2)
		self.assertEqual(self.rmq.query(2, 2), 7)

	def test_random_sequence(self):
		import random
		for test in xrange(100):
			n = random.randint(1, 100)
			A = []
			for i in xrange(n):
				A.append(random.randint(1, 1000))
			self.rmq.preprocess(A)
			for i in xrange(n):
				smaller = A[i]
				for j in xrange(i, n):
					smaller = min(smaller, A[j])
					self.assertEqual(self.rmq.query(i, j), smaller)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRMQ)
unittest.TextTestRunner(verbosity = 2).run(suite)
