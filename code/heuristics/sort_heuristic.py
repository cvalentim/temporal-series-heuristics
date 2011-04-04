from heuristic import Heuristic

class SortHeuristic(Heuristic):
	def preprocess(self, sequence):
		self.sequence = sequence
		self.pairs = []
		for i in xrange(len(self.sequence)): 
			for j in xrange(i + 1, len(self.sequence)):
				delta = self.sequence[j] - self.sequence[i]
				self.pairs.append((delta, i, j))
		self.pairs = sorted(self.pairs, key = lambda x: x[0], reverse = True)
				
	
	def query(self, query): 
		answers = []
		for delta, i, j in self.pairs:
			if delta >= query:
				answers.append((self.sequence[i], self.sequence[j]))
		return answers

	def __str__(self):
		return "SortHeuristic"
