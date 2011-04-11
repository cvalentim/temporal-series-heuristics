import io
import sys
import random
from executer import Executer

class OneDimExecuter(Executer):
	def _parse_line(self, line):
		if line.startswith("random"):
			n = int(line.split(" ")[1])
			res = [random.randint(0, 10000) for x in xrange(n)]
			return res
		line = line.split(',')
		res = [int(x) for x in line]
		return res
