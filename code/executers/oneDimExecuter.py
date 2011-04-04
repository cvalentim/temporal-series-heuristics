import io
import sys
from executer import Executer

class OneDimExecuter(Executer):
	def _parse_line(self, line):
		line = line.split(',')
		res = [int(x) for x in line]
		return res
