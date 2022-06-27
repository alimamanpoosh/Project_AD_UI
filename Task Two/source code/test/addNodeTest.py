import unittest

from graph.graph import *


class Test(unittest.TestCase):

    def test1(self):
        wg = WeightedGraph()

        wg.add_node("a")
        wg.add_node("b")
        wg.add_node("c")

        node1 = wg.nodes.get("a")
        self.assertIn(node1, wg.nodes.values())

        node2 = wg.nodes.get("b")
        self.assertIn(node2, wg.nodes.values())

        node3 = wg.nodes.get("c")
        self.assertIn(node3, wg.nodes.values())

        self.assertIn("a", wg.nodes.keys())
        self.assertIn("b", wg.nodes.keys())
        self.assertIn("c", wg.nodes.keys())