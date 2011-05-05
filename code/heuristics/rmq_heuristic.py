from heuristic import Heuristic

class RmqHeuristic(Heuristic):
	def create_delta_time(self, sequence):
		self.delta_time = [[] for x in xrange(len(sequence))]
		for i in xrange(0, len(self.sequence)):
			j = i + 1
			while j < len(sequence) and sequence[j - 1] <= sequence[j]:
				self.delta_time[j - i].append((i, sequence[j] - sequence[i]))
				j += 1
		for t in xrange(0, len(sequence)):
			self.delta_time[t] = sorted(self.delta_time[t],
										key = lambda x: x[1], reverse = True)

	# NOTE: this function looks out of context
	def preprocess_size(self):
		size = 0
		for t in xrange(self.delta_time):
			size += len(self.delta_time[t])
		return size
	
	def preprocess(self, sequence):
		self.sequence = sequence
		self.create_delta_time(sequence)
		
	def query(self, query): 
		answers = []
		return answers

	def __str__(self):
		return "RMQHeuristic"
