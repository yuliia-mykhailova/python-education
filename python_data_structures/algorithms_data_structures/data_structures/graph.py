"""Module for Graph realization"""
from algorithms_data_structures.data_structures.linked_list import LinkedList, Node


class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = LinkedList()

    def delete_edge(self, node):
        """Deletes edge node from the list of edges"""
        index = self.edges.lookup(node)
        self.edges.delete(index)


class Graph:
    """Class for graph implementation"""

    def __init__(self):
        """Constructor"""
        self.vertices = LinkedList()

    def __str__(self):
        return f'{self.vertices}'

    def __iter__(self):
        nodes = self.vertices

        for node in nodes:
            yield node.data

    def insert(self, data, connections):
        """Adds element to graph"""
        new_vertex = self.lookup(data)
        if not new_vertex:
            new_vertex = Vertex(data)
            self.vertices.append(new_vertex)
        for node in connections:
            vertex = self.lookup(node)
            if not vertex:
                vertex = Vertex(node)
                self.vertices.append(vertex)
            new_vertex.edges.append(vertex)
            vertex.edges.append(new_vertex)

    def lookup(self, data):
        """Return a vertex from graph"""
        for node in self.vertices:
            if node.data == data:
                return node
        return None

    def delete(self, vertex):
        """Deletes a vertex from a graph"""
        node = self.lookup(vertex)
        if not node:
            return
        connections = node.edges

        for connected_node in connections:
            connected_node.delete_edge(node)

        self.vertices.delete(self.vertices.lookup(node))

    def print_graph(self):
        for node in self.vertices:
            print(node.data, end=': ')
            for edge in node.edges:
                print(edge.data, end='; ')
            print()
