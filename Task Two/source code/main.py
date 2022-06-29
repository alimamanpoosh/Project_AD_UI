from graph.graph import *

if __name__ == '__main__':

    wg = WeightedGraph()

    wg.add_node("a")
    wg.add_node("b")
    wg.add_node("c")
    wg.add_node("d")

    wg.add_edge("a", "b", 1)
    wg.add_edge("b", "c", 2)

    wg.add_edge("a", "d", 2)
    wg.add_edge("d", "c", 1)

    WeightedGraph.get_all_shortest_path(wg, "a", "c")
