import math

"""
Sparse table RMQ implementation.
"""
class RMQSt:
	def __init__(self):
		pass

	def preprocess(self, A):
		n = len(A)
		k = int(math.log(n, 2))
		self.PD = [[-1]*(k + 1) for x in xrange(n)]
		self.ID = [[-1]*(k + 1) for x in xrange(n)]
		for i in xrange(n):
			self.PD[i][0] = A[i]
			self.ID[i][0] = i
		for delta in xrange(1, k + 1):
			for i in xrange(n):
				self.PD[i][delta] = self.PD[i][delta - 1]
				self.ID[i][delta] = self.ID[i][delta - 1]
				if i + 2**(delta - 1) < n:
					if self.PD[i][delta] > self.PD[i + 2**(delta-1)][delta-1]:
						self.PD[i][delta] = self.PD[i + 2**(delta-1)][delta-1]
						self.ID[i][delta] = self.ID[i + 2**(delta-1)][delta-1]

	def query(self, i, j):
		k = int(math.log(j - i + 1, 2))
		if self.PD[i][k] <= self.PD[j - 2**k + 1][k]:
			return self.ID[i][k]
		else:
			return self.ID[j - 2**k + 1][k]
