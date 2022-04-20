from typing import Dict, List


def print_tree(tree: Dict[int,List[int]]):
    for u in tree:
        print(u, ', '.join([str(x) for x in tree[u]]), sep='\t')
    