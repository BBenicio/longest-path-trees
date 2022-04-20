from tree_generator import generate_forest
from path import find_longest_path
from timeit import default_timer as timer

import pandas as pd
import tqdm


if __name__ == '__main__':
    results = []
    print('generating forest...')
    forest = generate_forest(range(2, 1001), count=100)
    print('forest generation done.')
    for tree in tqdm.tqdm(forest):
        start = timer()
        lp = find_longest_path(tree)
        end = timer()
        results.append({
            'n': len(tree),
            'longest_path': lp,
            'size': len(lp),
            'time': end - start
        })

    df = pd.DataFrame(results)
    df.to_csv('results.csv')
