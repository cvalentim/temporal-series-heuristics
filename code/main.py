from executers.twoDimExecuter import TwoDimExecuter
from executers.oneDimExecuter import OneDimExecuter
from heuristics.sort_heuristic import SortHeuristic
from heuristics.heap_heuristic import HeapHeuristic
from environment.environment import Environment

if __name__ == '__main__':
	exec_env = Environment()
	exec_env.evaluate('env.in')
