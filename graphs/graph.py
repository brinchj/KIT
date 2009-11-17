# coding: utf-8

class EdgeAlreadyExistsException(Exception):
    pass


class Node:
    def __init__(self):
        self.edges = []

    def add_edge(self, node):
        if self.has_edge(node):
            raise EdgeAlreadyExistsException(self, node)
        self.edges.append(node)

    def has_edge(self, node):
        return (node in self.edges)


class DirectedGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_nodes(self, nodes):
        self.nodes += nodes

    def get_nodes(self):
        return list(self.nodes)

    def add_edge(self, node0, node1):
        node0.add_edge(node1)

    def has_edge(self, node0, node1):
        return node0.has_edge(node1)

    def __repr__(self):
        return '\n'.join(map(repr, self.nodes))


class UndirectedGraph(DirectedGraph):
    def add_edge(self, node0, node1):
        node0.add_edge(node1)
        node1.add_edge(node0)



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


class PhoneGraph(DirectedGraph):
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
