import sys

"""
Implements a tree data structure.

Each vertex is a instance of class Node.
The tree is build by passing the edges 
(pairs of external nodes ids) to the method add_edge. 
Initialy the tree is unrooted but at any moment one
can call the method set_root passing a id and that way
rooting the tree.
"""

from heuristics.node import Node

class Tree:
	def __init__(self):
		self.m_id = {} # maps an external id to an internal
		self.nodes = [] # list of tree nodes
		self.root_id = None

	def _get_or_add_id(self, u):
		if self.m_id.has_key(u):
			return  self.m_id[u]
		else:
			id_u = len(self.m_id)
			new_node = Node(value = -1, _id = u, children = [])
			self.nodes.append(new_node)
			self.m_id[u] = id_u
			return id_u

	def _get_id(self, u):
		if self.m_id.has_key(u):
			return self.m_id[u]
		return -1
	
	def add_edge(self, u, v):
		id_u = self._get_or_add_id(u)
		id_v = self._get_or_add_id(v)
		node_u = self.nodes[id_u]
		node_v = self.nodes[id_v]
		self.nodes[id_u].children.append(node_v)
		self.nodes[id_v].children.append(node_u)

	def has_edge(self, u, v):
		id_u = self._get_id(u)
		id_v = self._get_id(v)
		if id_u == -1 or id_v == -1:
			return False
		return self.nodes[id_v] in self.nodes[id_u].children

	def set_root(self, u):
		node_u = self._get_id(u)
		if node_u == -1:
			return -1
		self.root_id = node_u
		return u

	def size(self):
		return len(self.nodes)

	def get_root(self):
		if self.root_id is None:
			print sys.stderr, "ERROR: root not set."	
			return None
		return self.nodes[self.root_id]

	def get_node(self, u):
		u_id = self._get_id(u)
		if u_id == -1:
			return None
		return self.nodes[u_id]	
