import unittest

from graph.graph import *


class Test(unittest.TestCase):

    def test1(self):
        g = WeightedGraph()

        g.add_node("a")
        g.add_node("b")
        g.add_node("c")

        g.add_edge("a", "b", 1)
        g.add_edge("b", "c", 2)
        g.add_edge("a", "c", 10)

        self.assertListEqual(g.get_shortest_path("a", "c").nodes, ["a", "b", "c"])
        self.assertEqual(3, g.dijkstra("a", "c"))
        self.assertEqual(2, g.dijkstra("c", "b"))

    def test2(self):
        wg = WeightedGraph()

        wg.add_node("a")
        wg.add_node("b")
        wg.add_node("c")
        wg.add_node("d")

        wg.add_edge("a", "b", 1)
        wg.add_edge("b", "c", 4)

        wg.add_edge("a", "d", 2)
        wg.add_edge("d", "c", 1)

        self.assertListEqual(wg.get_shortest_path("a", "c").nodes, ["a", "d", "c"])
        self.assertEqual(2, wg.dijkstra("a", "d"))
        self.assertEqual(3, wg.dijkstra("a", "c"))
        self.assertEqual(1, wg.dijkstra("a", "b"))