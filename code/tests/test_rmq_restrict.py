import random
import unittest

from heuristics.rmq_restrict import RMQRestrict

class TestRMQRestrict(unittest.TestCase):
	def setUp(self):
		self.rmq = RMQRestrict()

	def test_preprocess_blocks(self):
		block = [2, 3, 2, 1]
		self.rmq.blocks_ids = {}
		self.rmq.norm_b = []
		self.assertEqual(self.rmq.preprocess_blocks(block), 0)
		self.assertEqual(len(self.rmq.blocks_ids), 1)
		self.assertEqual(len(self.rmq.norm_b), 1)
		import pdb
		for i in xrange(0, len(block)):
			smaller = i
			for j in xrange(i, len(block)):
				if block[j] < block[smaller]:
					smaller = j
				self.assertEqual(self.rmq.norm_b[0][i, j], smaller)		

	def test_get_block_and_index(self):
		self.rmq.b_size = 3
		self.assertEqual(self.rmq.get_block_and_index(5), (1, 2))
		self.assertEqual(self.rmq.get_block_and_index(4), (1, 1))
		self.assertEqual(self.rmq.get_block_and_index(0), (0, 0))

	def test_preprocess_blocks_random(self):
		import random
		self.rmq.blocks_ids = {}
		self.rmq.norm_b = []
		for test in xrange(10):
				n = random.randint(1, 13)
				now = random.randint(0, 10000)
				block = [now]
				for i in xrange(n - 1):
					if random.randint(0,1) == 0:
						now -= 1
					else:
						now += 1
					block.append(now)
				block_id = self.rmq.preprocess_blocks(block)
				self.assertTrue(block_id <=  test + 1)
				self.assertTrue(len(self.rmq.blocks_ids) <=  test + 1)
				self.assertTrue(len(self.rmq.norm_b) <=  test + 1)
				import pdb
				for i in xrange(0, len(block)):
					smaller = i
					for j in xrange(i, len(block)):
						if block[j] < block[smaller]:
							smaller = j
						self.assertEqual(self.rmq.norm_b[block_id][i, j],
										 smaller)		
	
	
	def test_one_sequence(self):
		self.rmq.preprocess([2])
		# testando se ha lixo entre pesquisas
		self.assertEqual(self.rmq.query(0, 0), 2)	
	
	def test_two_sequence(self):
		self.rmq.preprocess([2, 1])
		self.assertEqual(self.rmq.query(0, 1), 1)
		self.assertEqual(self.rmq.query(0, 0), 2)
		self.assertEqual(self.rmq.query(1, 1), 1)

	
	def test_three_sequence(self):
		self.rmq.preprocess([1, 3, 2])
		self.assertEqual(self.rmq.query(0, 2), 1)
		self.assertEqual(self.rmq.query(0, 1), 1)
		self.assertEqual(self.rmq.query(1, 1), 3)
		self.assertEqual(self.rmq.query(1, 2), 2)
		self.assertEqual(self.rmq.query(2, 2), 2)
	
	
	def test_three_sequence_again(self):
		self.rmq.preprocess([4, 2, 3])
		self.assertEqual(self.rmq.query(0, 2), 2)
		self.assertEqual(self.rmq.query(0, 1), 2)
		self.assertEqual(self.rmq.query(0, 0), 4)
		self.assertEqual(self.rmq.query(1, 2), 2)
		self.assertEqual(self.rmq.query(1, 1), 2)
		self.assertEqual(self.rmq.query(2, 2), 3)

	def test_random_sequence(self):
		import random
		for test in xrange(100):
			n = random.randint(1, 1000)
			A = []
			for i in xrange(n):
				A.append(random.randint(1, 100))
			self.rmq.preprocess(A)
			for i in xrange(n):
				smaller = A[i]
				#smaller_id = i
				for j in xrange(i, n):
					if smaller >  A[j]:
						smaller = A[j]	
					#	smaller_id = j
					#self.assertEqual(self.rmq.query(i, j), smaller_id)
					self.assertEqual(self.rmq.query(i, j), smaller)
	
suite = unittest.TestLoader().loadTestsFromTestCase(TestRMQRestrict)
unittest.TextTestRunner(verbosity = 2).run(suite)
