import io
import sys
import random

from executer import Executer

class TwoDimExecuter(Executer):
	def _parse_line(self, line):
		if line.startswith("random"):
			if len(line.split(" ")) <= 1:
				print sys.stderr, "Must include the amount of \
								  number in the random sequence."
				return None
			try:
				n = int(line.split(" ")[1])
			except ValueError:
				print sys.stderr, "Format is random <integer>."
				return None
			return [random.randint(1, 10000) for x in xrange(n)]
		line = line.replace('(', ' ').replace(')', ' ')
		line = line.split(',')
		if len(line)%2 != 0 or len(line) < 2:
			return None
		res = []
		i = 0
		while i < len(line) - 1:
			res.append((int(line[i]), int(line[i + 1])))
			i += 2
		print res	
		return res

