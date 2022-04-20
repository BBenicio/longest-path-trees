from typing import Dict, List, Union
import numpy as np

from tree_generator import generate_random_tree
from utils import print_tree


def find_longest_path(tree: Dict[int, List[int]]) -> List[int]:
    u = 0
    distances = bfs(tree, u)
    x_list = np.argwhere(np.array(distances) == max(distances)).flatten()
    longest_path = (u, u)
    longest_path_size = 0
    for x in x_list:
        distances = bfs(tree, x)
        if max(distances) > longest_path_size:
            longest_path_size = max(distances)
            longest_path = (x, np.argmax(distances))

    return bfs(tree, longest_path[0], longest_path[1])


def bfs(graph: Dict[int, List[int]], root: int, return_path_to: Union[int, None] = None) -> List[int]:
    visited = [False for _ in graph]
    visited[root] = True
    to_visit = [root]
    distances = [0 for _ in graph]
    pred = [None for _ in graph]
    while len(to_visit) > 0:
        u = to_visit.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                pred[v] = u
                to_visit.append(v)

    if return_path_to:
        v = return_path_to
        path = [v]
        while pred[v] != None:
            path.append(pred[v])
            v = pred[v]
        path.reverse()

        return path

    return distances


if __name__ == '__main__':
    tree = generate_random_tree(5)
    print_tree(tree)
    path = find_longest_path(tree)
    print('longest path size:', len(path))
    print('longest path:', ', '.join([str(x) for x in path]))
