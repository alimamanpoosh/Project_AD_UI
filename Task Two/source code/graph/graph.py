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


class Node:
    def __init__(self, label: str):
        self.__label = label
        self.__edges = []

    @property
    def edges(self):
        return self.__edges

    @property
    def label(self):
        return self.__label

    def add_edge(self, target, weight: int):
        edge = Edge(self, target, weight)
        self.edges.append(edge)

    def __str__(self):
        return f"{self.__label}"


class Edge:

    def __init__(self, from_node: Node, to_node: Node, weight: int):
        self.__from_node: Node = from_node
        self.__to_node: Node = to_node
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
        return f"{str(self.__from_node)} -> {str(self.__to_node)}"


class WeightedGraph:

    def __init__(self):
        self.__nodes = {}  # key: String  value: Node

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, label: str):
        self.nodes[label] = Node(label)

    def add_edge(self, from_node: str, to_node: str, weight: int):
        origin: Node = self.nodes.get(from_node)
        target: Node = self.nodes.get(to_node)

        if not origin or not target:
            raise Exception("There is not Node for creating Edge")

        origin.add_edge(target, weight)
        target.add_edge(origin, weight)

    def get_shortest_path(self, from_node, to_node):
        from_node: Node = self.nodes.get(from_node)
        to_node: Node = self.nodes.get(to_node)

        if not from_node or not to_node:
            raise Exception("There is not Node for finding the shortest path")

        distances = dict()  # key: Node  value:  Integer

        for node in self.nodes.values():
            distances[node] = sys.maxsize

        distances[from_node] = 0

        visited = set()

        queue = PriorityQueue()
        queue.put((0, from_node))

        previous = dict()  # key: Node  value: Node

        while not queue.empty():

            current: Node = queue.get()[1]
            visited.add(current)

            for edge in current.edges:
                if edge.to_node in visited:
                    continue

                new_distance = distances.get(current) + edge.weight

                if new_distance < distances.get(edge.to_node):
                    distances[edge.to_node] = new_distance
                    previous[edge.to_node] = current
                    queue.put((new_distance, edge.to_node))

        return WeightedGraph.__build_path(previous, to_node)

    @classmethod
    def __build_path(cls, previous: dict, to_node: Node) -> Path:
        stack = [to_node]
        previous_node = previous.get(to_node)

        while previous_node:
            stack.append(previous_node)
            previous_node: Node = previous.get(previous_node)

        p = Path()
        while stack:
            p.add_node(stack.pop().label)

        return p

    def print_graph(self):
        for node in self.nodes.values():
            s = ""
            for e in node.edges:
                s = s + str(e.to_node) + ","
            print(node, " is connected to ", s)