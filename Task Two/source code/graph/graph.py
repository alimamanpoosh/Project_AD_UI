import sys
from queue import PriorityQueue


class Path:
    def __init__(self):
        self.__nodes = []

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, label: str):
        self.nodes.append(label)

    def __str__(self):
        return f"{self.__nodes}"


class Edge:
    def __init__(self, from_node: None, to_node: str, weight: int):
        self.__from_node = from_node
        self.__to_node = to_node
        self.__weight = weight

    @property
    def from_node(self):
        return self.__from_node

    @property
    def to_node(self):
        return self.__to_node

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__from_node} -> {self.__to_node}"


class Node:
    def __init__(self, label: str):
        self.__label = label
        self.__edges = []

    @property
    def edges(self):
        return self.__edges

    def add_edge(self, target, weight: int):
        self.__edges.append(Edge(self, target, weight))

    def __str__(self):
        return self.__label


class WeightedGraph:

    def __init__(self):
        self.__nodes = {}  # key: String  value: Node

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, label: str):
        self.nodes[label] = Node(label)

    def add_edge(self, from_node: str, to_node: str, weight: int):
        from_node: Node = self.nodes.get(from_node)
        to_node: Node = self.nodes.get(to_node)

        if not from_node or not to_node:
            raise Exception("There is not Node for creating Edge")

        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)

