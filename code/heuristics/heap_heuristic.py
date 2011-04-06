import heapq

class HeapHeuristic:
	def preprocess(self, sequence):
		self.pairs = []
		self.sequence = sequence
		for i in xrange(len(self.sequence)):
			for j in xrange(i + 1, len(self.sequence)):
				delta = self.sequence[j] - self.sequence[i]
				# adding a negative delta since heapq is a minimum heap
				self.pairs.append((-delta, i, j))
		self.heap = heapq.heapify(self.pairs)
		self.heap_c = heapq.heapify(self.pairs)
		del self.pairs

	def query(self, query):
		answers = []
		while True:
			try:
				delta, i, j = heapq.heappop(self.heap)
				# actually we want positive delta
				delta = (-1) * delta 
			except IndexError:
				break
			if delta >= query:
				answers.append((self.sequence[i], self.sequence[j]))
			else:
				break
		self.heap = self.heap_c.copy()
