import math
from heuristics.rmq_st import RMQSt

class RMQRestrict:
	def __init__(self):
		pass

	"""
	Normalizes block and memorizes all solutions
	for this block. 

	Returns a b_id which can be used to retrive
	solutions in this block. It is important to remember
	that the solutions inside a block is an 0-based index.
	"""
	def preprocess_blocks(self, block):
		nblock = [0]*len(block)
		for j in xrange(1, len(block)):
			nblock[j] = block[j] - block[j - 1]

		if self.blocks_ids.has_key(tuple(nblock)):
			return self.blocks_ids[tuple(nblock)]
		else:
			b_id = len(self.blocks_ids)
			self.blocks_ids[tuple(nblock)] = b_id
			m_ij = {}
			for i in xrange(len(block)):
				smaller = i
				for j in xrange(i, len(block)):
					if block[smaller] > block[j]:
						smaller = j
					m_ij[i, j] = smaller
			self.norm_b.append(m_ij)
			assert len(self.norm_b) == len(self.blocks_ids)
			return b_id
		

	def preprocess(self, A):
		self.n = len(A)
		self.A = A
		self.b_size = int(math.log(self.n, 2)/2) + 1

		self.blocks = [] # list of minimums for each block of size b_size
		self.where = [] # keeps the index of the minimum of the block
		self.blocks_ids = {}
		self.norm_b = []
		self.b_unique = [] # keeps a map between block position
						  # and its normalized index, dont need to be a map

		smaller = A[0]
		block = [A[0]]
		smaller_id = 0

		for i in xrange(1, self.n):
			if len(block) == self.b_size:
				self.blocks.append(smaller)
				self.where.append(smaller_id)
				b_id = self.preprocess_blocks(block)
				self.b_unique.append(b_id)
				block = [A[i]]
				smaller = A[i]
				smaller_id = i
			else:
				block.append(A[i])
				if smaller > A[i]:
					smaller = A[i]
					smaller_id = i

		self.blocks.append(smaller)
		self.where.append(smaller_id)
		b_id = self.preprocess_blocks(block)
		self.b_unique.append(b_id)

		assert len(self.blocks) == (self.n - 1)/self.b_size + 1
		assert len(self.blocks) == len(self.where)
		self.rmq_st = RMQSt()
		self.rmq_st.preprocess(self.blocks)

	def get_block_and_index(self, i):
		block_i = i/self.b_size
		index_i = i%self.b_size
		return (block_i, index_i)
		
	def query(self, i, j):
		assert i <= j
		block_i, index_i = self.get_block_and_index(i)
		block_j, index_j = self.get_block_and_index(j)

		# WARNING: change me later, ineficient
		if block_i != block_j:
			ans_value = self.A[i]
			ans_index = i
			if block_i + 1 <  block_j:
				bid = self.rmq_st.query(block_i + 1, block_j - 1)
				ans_value = self.blocks[bid]
				ans_index = self.where[bid]
			
			id_bi = self.b_unique[block_i]
			id_bj = self.b_unique[block_j]	

			id_min_in_bi = block_i * self.b_size + \
							self.norm_b[id_bi][index_i, self.b_size - 1]

			id_min_in_bj = block_j * self.b_size + \
							self.norm_b[id_bj][0, index_j]
			
			if self.A[id_min_in_bi] < ans_value:
				ans_value = self.A[id_min_in_bi]
				ans_index = id_min_in_bi

			if self.A[id_min_in_bj] < ans_value:
				ans_value = self.A[id_min_in_bj]
				ans_index = id_min_in_bj

			return ans_index
		else:
			b_id = self.b_unique[block_i]
			id_min = block_i * self.b_size + \
					self.norm_b[b_id][index_i, index_j]
			return id_min
