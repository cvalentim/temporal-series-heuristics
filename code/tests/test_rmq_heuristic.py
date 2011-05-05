import random
import unittest

from heuristics.rmq_heuristic import RmqHeuristic

class TestRmqHeuristicMatching(unittest.TestCase):
	def setUp(self):
		self.heuristic = RmqHeuristic()
	
	def test_preprocessing_delta_time(self):
		self.heuristic = RmqHeuristic()
		self.heuristic.preprocess([3, 4, 6, 9])
		self.assertEqual(len(self.heuristic.delta_time), 4)
		self.assertEqual(len(self.heuristic.delta_time[0]), 0)
		self.assertEqual(self.heuristic.delta_time[1], 
							[(2, 3), (1, 2), (0, 1)]) 
		self.assertEqual(self.heuristic.delta_time[2], [(1, 5), (0, 3)])
		self.assertEqual(self.heuristic.delta_time[3], [(0, 6)])

	def test_empty_sequence(self):
		self.heuristic.preprocess([])
		self.assertEqual(self.heuristic.query(7), [])
		# testando se ha lixo entre pesquisas
		self.assertEqual(self.heuristic.query(10), [])	

	def test_sequence_size_one(self):
		self.heuristic.preprocess([3])
		self.assertEqual(self.heuristic.query(10), [])

	def test_sequence_size_two(self):
		self.heuristic.preprocess([3, 1])
		self.assertEqual(self.heuristic.query(10), [])
		# vazio pela ordem dos numeros
		self.assertEqual(self.heuristic.query(0), [])
		
		self.heuristic.preprocess([1, 3])
		self.assertEqual(self.heuristic.query(10), [])
		self.assertEqual(self.heuristic.query(0), [(1, 3)])

	def test_equal_values_sequence(self):
		self.heuristic.preprocess([1]*100)
		self.assertEqual(self.heuristic.query(1), [])	
		self.assertEqual(len(self.heuristic.query(0)), (100*99)/2)

	def test_arithmetic_sequence(self):
		# sequencia de 1 ate 100
		self.heuristic.preprocess(range(1, 101))
		self.assertEqual(self.heuristic.query(99), [(1, 100)])	
		# todos os pares tem diferenca maior ou igual a 1
		self.assertEqual(len(self.heuristic.query(1)), (100 * 99)/2)
		answers98 = self.heuristic.query(98)
		self.assertEqual(len(answers98), 3)
		self.assertTrue((1, 100) in answers98)
		self.assertTrue((1, 99) in answers98)
		self.assertTrue((2, 100) in answers98)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRmqHeuristicMatching)
unittest.TextTestRunner(verbosity = 2).run(suite)
