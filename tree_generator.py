from typing import Dict, Iterable, List
import numpy as np


def generate_random_tree(n: int = 2) -> Dict[int, List[int]]:
    if n <= 1:
        raise AttributeError('n must be greater than or equal to 2')

    graph = {}
    unconnected = set((i for i in range(n)))
    connected = set()
    while len(unconnected) > 0:
        v = np.random.choice(list(connected)) if len(
            connected) > 0 else unconnected.pop()
        w = unconnected.pop()

        if v not in graph:
            graph[v] = []
        if w not in graph:
            graph[w] = []
        graph[v].append(w)
        graph[w].append(v)

        connected.add(v)
        connected.add(w)
        if v in unconnected:
            unconnected.remove(v)
        if w in unconnected:
            unconnected.remove(w)

    return graph


def generate_forest(trees_node_counts: Iterable[int] = range(2, 40), count: int = 10) -> List[Dict[int, List[int]]]:
    forest = []
    for n in trees_node_counts:
        for _ in range(count):
            forest.append(generate_random_tree(n))

    return forest
