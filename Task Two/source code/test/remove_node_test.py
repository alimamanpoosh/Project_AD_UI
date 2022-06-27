import unittest

from graph.graph import *


class Test(unittest.TestCase):

    def test1(self):
        wg = WeightedGraph()
        wg.add_node("a")
        wg.add_node("b")
        wg.add_node("c")
        wg.add_node("d")

        wg.add_edge("a", "b", 1)
        wg.add_edge("b", "c", 2)

        wg.add_edge("a", "d", 2)
        wg.add_edge("d", "c", 1)

        node1: Node = wg.nodes.get("a")
        node2 = wg.nodes.get("b")
        node4 = wg.nodes.get("c")

        target_node = wg.nodes.get("c")

        self.assertIn(target_node, wg.nodes.values())
        wg.remove_node("c")

        self.assertNotIn(target_node, wg.nodes.values())
        self.assertIn("a", wg.nodes.keys())
        self.assertIn("b", wg.nodes.keys())
        self.assertIn("d", wg.nodes.keys())

        node1_adjacency_list = []
        for edge in node1.edges:
            node1_adjacency_list.append(edge.to_node)
        self.assertNotIn(target_node, node1_adjacency_list)

        node2_adjacency_list = []
        for edge in node2.edges:
            node2_adjacency_list.append(edge.to_node)
        self.assertNotIn(target_node, node2_adjacency_list)

        node4_adjacency_list = []
        for edge in node4.edges:
            node4_adjacency_list.append(edge.to_node)
        self.assertNotIn(target_node, node4_adjacency_list)
