# -*- coding: utf-8 -*-

class NodeAlreadyExistsError(Exception):
    """ Knuden findes allerede """
    pass

class NoSuchNodeError(Exception):
    """ Knuden findes ikke """
    pass

class EdgeAlreadyExistsException(Exception):
    """ Kanten findes allerede """
    pass

class NoSuchEdgeError(Exception):
    """ Kanten findes ikke """
    pass


class Graph:
  def __init__(self):
      """ Tom graf, ingen knuder """
      self.nodes = []

  def add_node(self, node):
      """ Tilføj en knude """
      # Fejlhåndtering
      self.ensure_nodes( [node], False )
      # Tilføj knuden
      self.nodes.append(node)

  def del_node(self, node):
      """ Slet en knude """
      # Fejlhåndtering
      self.ensure_nodes( [node], True )
      # Slet knuden
      self.nodes.remove(node)

  def get_nodes(self):
      """ Hent en kopi af grafens knuder """
      return list(self.nodes)

  def get_edges(self):
      """ Hent en kopi af kant-par """
      edges = []
      for node_a in self.get_nodes():
          for node_b in node.get_edges():
              # tilføj kant fra a til b
              edges.append( (node_a, node_b) )
      return edges


  def add_edge(self, node_a, node_b):
      """ Tilføjer en kant fra a til b """
      # Fejlhåndtering
      self.ensure_nodes(  [node_a, node_b] , True  )
      self.ensure_edges( [(node_a, node_b)], False )
      # Tilføj kant
      node_a.add_edge(node_b)

  def del_edge(self, node_a, node_b):
      """ Sletter kanten fra a til b """
      # Fejlhåndtering
      self.ensure_edges( [(node_a, node_b)], True )
      # Slet kant
      node_a.del_edge(node_b)

  def has_node(self, node):
      """ Undersøger om node ligger i grafen """
      return (node in self.nodes)

  def has_edge(self, node_a, node_b):
      """ Undersøger om en kant fra a til b findes """
      return node_a.has_edge(node_b)

  def count_nodes(self):
      """ Tæller antallet af knuder """
      return len(self.nodes)

  def count_edges(self):
      """ Tæller antallet af kanter """
      count = 0
      for node_a in self.nodes:
          # Læg a's kanter til
          count += node_a.count_edges()
      return count

  def reset_colors(self):
      for node in self.get_nodes():
          node.set_color(0)


  def depth_first_no_reset(self, node):
      """ Udfør dybde-først søgning antaget at farverne er OK """
      node.set_color(1)
      nodes = [node]
      for edge_node in node.get_edges():
          if edge_node.get_color() == 0:
              nodes += self.depth_first_no_reset(edge_node)
      return nodes

  def depth_first(self, node):
      """ Udfør dybde-først søgning udfra knude """
      self.reset_colors()
      return self.depth_first_no_reset(node)


  def breadth_first(self, node):
      """ Udfør bredde-først søgning udfra knude """
      self.reset_colors()
      nodes, queue = [], [node]
      node.set_color(1)
      while len(queue) > 0:
          node = queue.pop(0)
          nodes.append(node)
          for edge_node in node.get_edges():
              if edge_node.get_color() == 0:
                  edge_node.set_color(1)
                  queue.append(edge_node)
      return nodes


  def ensure_nodes(self, nodes, must_exist):
      """ Kast en fejl hvis en af knuderne findes/ikke findes """
      for node in nodes:
          # Findes knuden?
          exists = self.has_node(node)
          # Overholder den begrænsningen?
          if must_exist and not exists:
              raise NoSuchNodeError(node)
          if not must_exist and exists:
              raise NodeAlreadyExistsError(node)

  def ensure_edges(self, edges, must_exist):
      """ Kast en fejl hvis en af kanterne findes/ikke findes """
      for node_a, node_b in edges:
          # Findes knuden?
          exists = self.has_edge(node_a, node_b)
          # Overholder den begrænsningen?
          if must_exist and not exists:
              raise NoSuchEdgeError((node_a, node_b))
          if not must_exist and exists:
              raise EdgeAlreadyExistsError((node_a, node_b))



class DirectedGraph(Graph):
    """ Implementation af en orienteret graf """
    pass


class UndirectedGraph(Graph):
    """ Implementation af en ikke-orienteret graf """

    def add_edge(self, node0, node1):
        """ Tilføjer en kant til grafen """
        Graph.add_edge(self, node0, node1)
        Graph.add_edge(self, node1, node0)

    def del_edge(self, node0, node1):
        """ Fjerner en kant fra grafen """
        Graph.del_edge(self, node0, node1)
        Graph.del_edge(self, node1, node0)

    def count_edges(self):
        """ Tæller antallet af kanter i grafen """
        # Divider med to, da alle kanter ligger dobbelt
        # (en for hver retning)
        return Graph.count_edges(self) / 2


class Node:
    def __init__(self):
        """ Ny knude, ingen kanter """
        self.edges = []
        self.color = 0

    def add_edge(self, node):
        """ Tilføj kant """
        self.edges.append(node)

    def get_edges(self):
        """ Hent kanter """
        return list(self.edges)

    def del_edge(self, node):
        """ Fjern kant """
        self.edges.remove(node)

    def has_edge(self, node):
        """ Test om en kant findes """
        return (node in self.edges)

    def count_edges(self):
        """ Tæl antallet af kanter """
        return len(self.edges)

    def set_color(self, color):
        """ Sæt knudens farve/markering """
        self.color = color

    def get_color(self):
        """ Hent knudens farve/markering """
        return self.color
