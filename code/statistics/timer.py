from time import clock
import datetime


"""
"""
class Timer:
	def __init__(self):
		self.start_t = datetime.datetime.now()

	def start(self):
		self.start_t = datetime.datetime.now()

	def end(self):
		self.end_t = datetime.datetime.now()

	def elapsed(self):
		if self.end_t is None or self.start_t is None:
			print >>sys.stderr, "Tempo nao medido corretamente."
			return None
		return (self.end_t - self.start_t).microseconds
