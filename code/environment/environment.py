import io
import sys

class Environment:
	def __int__(self, input_file = 'config.in'):
		self.input_file = input_file

	def help(self):
		pass

	def _clean_config(self, lines):
		config = {}
		for line in lines:
			if line.strip() == "":
				continue
			if line.startswith('#'):
				continue
			param = line.split(':')[0].strip()
			value = line.split(':')[1].strip()
			config[param] = value
		if 'problem' not in config:
			print >>sys.stderr, "You have to specifiy a problem type."
			self.help()
			return None

		if 'algorithms' not in config:
			print >>sys.stderr, "You have to specify at least one algorithm."
			self.help()
			return None
		else:
			config['algorithms'] = config['algorithms'].strip().split(',')
		
		if 'instances' not in config:
			print >>sys.stderr, "You have tospecify at least one instance file."
			self.help()	
			return None
		else:
			config['instances'] = config['instances'].strip().split(',')
		return config

	def get_alg(self, alg):
		if alg == "SortHeuristic":	
			from heuristics.sort_heuristic import SortHeuristic
			return SortHeuristic()			

	def _parse_config(self, config_path):
		try:
			fconfig = io.open(config_path, 'r')
		except IOError:
			print >>sys.stderr, "Could not open %s"%config_path
			return None
		input_lines = fconfig.readlines()
		fconfig.close()
		config_user = self._clean_config(input_lines)
		if config_user is None:
			return None
		config_internal = {}

		if config_user['problem'] == 'all_pairs_one_dim':
			from executers.oneDimExecuter import OneDimExecuter
			config_internal['executer'] = OneDimExecuter()
		
		config_internal['algorithms'] = []
		for algo in config_user['algorithms']:
			config_internal['algorithms'].append(self.get_alg(algo))
		
		config_internal['instances'] = config_user['instances']	
		return config_internal

	
	def evaluate(self, input_file = None):
		if input_file is not None:	
			self.input_file = input_file
		print "Using %s as evaluation config..."%self.input_file
		config = self._parse_config(self.input_file)
		if config is None:
			return False
		self.executer = config['executer']	
		for input_path in config['instances']:
			self.executer.load(input_path)
			self.executer.execute(config['algorithms'])
