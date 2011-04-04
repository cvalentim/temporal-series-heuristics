import io
import sys


class Executer:
	def __init__(self, heuristic = None, sequence = None, queries = None):
		self.heuristic = heuristic
		self.sequence = sequence
		self.queries = queries

	def execute(self):
		if self.heuristic is None:
			print >>sys.stderr, "Nao ha heuristica a ser executada."
			return False	
		if self.sequence is None or self.queries is None:
			print >>sys.stderr, "Sequencia ou pesquisas nao informada."
			return False
		print "Executando heuristica ", self.heuristic, "..."
		print "Sequencia de entrada ", self.sequence
		self.heuristic.preprocess(self.sequence)
		print "-------------------------"
		for query in self.queries:
			print "Pesquisa: ", query
			answers = self.heuristic.query(query)
			print answers
			print ""

	def _parse_line(self, line):
		raise NotImplemented 

	def load(self, input_path = 'input.in'):
		try:
			input_stream = io.open(input_path, 'r')
		except IOError:
			print >>sys.stderr, "Nao foi possivel abrir o arquivo de entrada."
			return False
		input_lines = input_stream.readlines()
		input_stream.close()
		where = 0
		sequence = None
		queries = []
		for where in xrange(len(input_lines)):
			line = input_lines[where]
			if line[0] == '#':
				print line 
				continue
			if line.strip() == "": # blank line
				continue 
			if sequence is None:
				# the first non-comment and non-blank line is the sequence
				sequence = self._parse_line(line)
				if sequence is None:
					print >>sys.stderr, "A sequencia de entrada nao esta\
						 formatada corretamenete."
					return False
			else:
				# if the sequence was read then it must to be a query
				query = self._parse_line(line)
				if query is None:
					print >>sys.stderr, "Alguma pesquisa nao esta corretamente formatada."
					return False
				if len(query) > 1: # more then one query per line
					print >>sys.stderr, "Mais de um pesquisa por linha."
					return False		
				queries.append(query[0])
		if len(queries) == 0 or sequence is None:
			print >>sys.stderr, "Erro ao ler ao ler a sequencia de entrada."
			return False
		self.sequence = sequence
		self.queries = queries

