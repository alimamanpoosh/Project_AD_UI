import unittest

from graph.graph import *


class Test(unittest.TestCase):

    def test1(self):
        wg = WeightedGraph()

        wg.add_node("a")
        wg.add_node("b")
        wg.add_node("c")

        wg.add_edge("a", "b", 1)
        wg.add_edge("b", "c", 2)
        wg.add_edge("c", "a", 10)

        self.assertTrue(wg.has_cycle())

    def test3(self):
        wg = WeightedGraph()

        wg.add_node("a")
        wg.add_node("b")
        wg.add_node("c")

        wg.add_edge("a", "b", 1)
        wg.add_edge("b", "c", 2)

        self.assertFalse(wg.has_cycle())