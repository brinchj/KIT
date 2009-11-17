# coding: utf-8

class NodeAlreadyExistsError(Exception):
    pass

class NoSuchNodeError(Exception):
    pass

class EdgeAlreadyExistsException(Exception):
    pass

class NoSuchEdgeError(Exception):
    pass


class Graph:
  def __init__(self):
      self.nodes = []

  def add_node(self, node):
      if node in self.nodes:
          raise NodeAlreadyExistsError()
      self.nodes.append(node)

  def del_node(self, node):
      if not node in self.nodes:
          raise NoSuchNodeError()
      self.nodes.remove(node)

  def get_nodes(self):
      return list(self.nodes)

  def add_edge(self, node_a, node_b):
      if self.has_edge(node_a, node_b):
          raise EdgeAlreadyExistsError()
      node_a.add_edge(node_b)

  def del_edge(self, node_a, node_b):
      if not self.has_edge(node_a, node_b):
          raise NoSuchEdgeError()
      node_a.del_edge(node_b)

  def has_node(self, node):
      return (node in self.nodes)

  def has_edge(self, node_a, node_b):
      return node_a.has_edge(node_b)

  def count_nodes(self):
      return len(self.nodes)

  def count_edges(self):
      count = 0
      for node in self.nodes:
          count += node.count_edges()
      return count


class UndirectedGraph(Graph):
    def add_edge(self, node0, node1):
        Graph.add_edge(self, node0, node1)
        Graph.add_edge(self, node1, node0)

    def del_edge(self, node0, node1):
        Graph.del_edge(self, node0, node1)
        Graph.del_edge(self, node1, node0)

    def count_edges(self):
        return Graph.count_edges(self) / 2


class Node:
    def __init__(self):
        self.edges = []

    def add_edge(self, node):
        self.edges.append(node)
    def del_edge(self, node):
        self.edges.remove(node)

    def has_edge(self, node):
        return (node in self.edges)

    def count_edges(self):
        return len(self.edges)


class Person(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name

    def get_friends(self):
        return list(self.edges)

    def __repr__(self):
        return self.name


class FriendGraph(UndirectedGraph):
    def add_person(self, person):
        self.add_node(person)

    def add_friends(self, person0, person1):
        self.add_edge(person0, person1)


class PhoneGraph(Graph):
    def add_person(self, person0):
        self.add_node(person0)

    def add_number(self, person0, person1):
        self.add_edge(person0, person1)


# Lav nogle personer
ps = [ Person('Navn%i' % i) for i in range(20) ]

# Lav en ny vennegraf
g = FriendGraph()

# Tilføj personer til graf
for p in ps:
    g.add_node(p)

# Tilføj nogle tilfældige relationer
import random
for i in range(len(ps)):
    p0 = p1 = None
    while p0 == p1:
        p0 = random.choice(ps)
        p1 = random.choice(ps)
    if not g.has_edge(p0, p1):
        g.add_edge(p0, p1)

for person in g.get_nodes():
    print person, person.get_friends()
