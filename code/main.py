from executers.twoDimExecuter import TwoDimExecuter
from executers.oneDimExecuter import OneDimExecuter
from heuristics.sort_heuristic import SortHeuristic
from heuristics.heap_heuristic import HeapHeuristic

if __name__ == '__main__':
	sort_heuristic = SortHeuristic()
	executer = OneDimExecuter(heuristics = [sort_heuristic])
	executer.load('one_dim_input.in')
	executer.execute()
