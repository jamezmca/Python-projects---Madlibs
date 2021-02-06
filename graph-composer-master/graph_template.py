# this is our markov chain representation
import random

# define the graph in terms of vertices

class Vertex:
    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbor_weights = []

    def add_edge_to(self, vertex, weight = 0):
        # this is adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight
        
    def increment_edge(self, vertex):
        # this is incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbor_weights.append(weight)


    def next_word(self):
        # randomly select next word ***based on weights!!!
        return random.choices(self.neighbors, weights = self.neighbor_weights)[0]

# now that we have our vertex representation, we put this together in a graph
class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # what are the values of all the vertices?
        # return all possible words
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # what if the value isn't in the graph
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value] # get the vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()

