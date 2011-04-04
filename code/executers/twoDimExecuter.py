import io
import sys

from executer import Executer

class TwoDimExecuter(Executer):
	def _parse_line(self, line):
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

