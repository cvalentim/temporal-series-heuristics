import math

class RMQ:
	def __init__(self):
		pass

	def preprocess(self, A):
		n = len(A)
		k = int(math.log(n, 2))
		self.PD = [[-1]*(k + 1) for x in xrange(n)]
		for i in xrange(n):
			self.PD[i][0] = A[i]
		for delta in xrange(1, k + 1):
			for i in xrange(n):
				self.PD[i][delta] = self.PD[i][delta - 1]
				if i + 2**(delta - 1) < n:
					self.PD[i][delta] = min(self.PD[i][delta], 
										self.PD[i + 2**(delta - 1)][delta - 1])

	def query(self, i, j):
		k = int(math.log(j - i + 1, 2))
		return min(self.PD[i][k], 
					self.PD[j - 2**k + 1][k])
