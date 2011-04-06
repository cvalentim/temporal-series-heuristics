from time import clock


"""
"""
class Timer:
	def __init__(self):
		self.start_t = clock()

	def start(self):
		self.start_t = clock()

	def end(self):
		self.end_t = clock()

	def elapsed(self):
		if self.end_t is None or self.start_t is None:
			print >>sys.stderr, "Tempo nao medido corretamente."
			return None
		return self.end_t - self.start_t
