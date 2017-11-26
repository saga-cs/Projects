from collections import defaultdict
from collections import deque
import unittest

class Graph:
	""" Class to implement a graph and its methods."""
	def __init__(self,Edges=None):
		self.Edges=Edges
		self.dic = defaultdict(list)
		for i in self.Edges:
			self.dic[i[0]].append(i[1])
			self.dic[i[1]].append(i[0])

	def add_node(self,node):
		"""Function that adds a node to a graph."""
		self.node=node
		self.dic.update({self.node:[]})
	
	def __getitem__(self,index):
		return self.dic[index]

	def add_edge(self,edge):
		"""Function that adds an edge between two nodes in a graph."""
		self.Edges.append(edge)
		self.dic[edge[0]].append(edge[1])
		self.dic[edge[1]].append(edge[0])

	def __iter__(self):
		return iter(self.dic.keys())

	def bfs(self,start):
		"""Function to calculate shortest distance of nodes from a starting node."""
		self.start=start
		color = dict()
		d = dict()
		for v in self.dic.keys():
			color.update({v:'white'})
			d.update({v:float('inf')})
		color[self.start] = 'grey'
		d[self.start] = 0
		Q=deque(str(self.start))
		while len(Q)!=0:
			u = Q.popleft()
			for v in self.dic[int(u)]:
				if color[v]=='white':
					color[v] = 'grey'
					d[v] = d[int(u)]+1
					Q.append(str(v))
			color[u] = 'black'
		return ((i, d[i]) for i in self.dic.keys())

	def distance(self,a,b):
		"""Function to calculate shortest distance between two nodes in a graph."""
		self.a=a
		self.b=b
		d=[]
		for node,dist in self.bfs(self.a):
			d.append((node,dist))
		for i in d:
			if i[0] == self.b:
				return i[1]

class GraphTest(unittest.TestCase):
	
	def test_add_node(self):
		edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
		g = Graph(edges)
		g.add_node(7)
		self.assertEqual(7 in g.dic.keys(),True)

	def test_add_edge(self):
		edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
		g = Graph(edges)
		g.add_edge((3,5))
		self.assertEqual((3 in g.dic[5] and 5 in g.dic[3]),True)


	def test_in(self):
		edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
		g = Graph(edges)
		self.assertEqual(4 in g , True)

	def test_Graph_indexing(self):
		edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
		g = Graph(edges)
		self.assertEqual(g[5], [1,2,4])

	def test_bfs(self):
		edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
		g = Graph(edges)
		self.assertEqual([(node,dist) for node, dist in g.bfs(1)], [(1,0),(2,1),(5,1),(3,2),(4,2),(6,3)])

	def test_distance(self):
		edges = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
		g = Graph(edges)
		self.assertEqual(g.distance(2,4), 2)


if __name__ == '__main__':
	unittest.main()
	