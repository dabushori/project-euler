from itertools import chain, combinations

def subsets(iterable, min_size, max_size):
    """
    Get all the subsets of iterables of sizes min_size to max_size (inclusive)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(min_size, max_size + 1))

def powerset(iterable):
    return subsets(iterable, 0, len(iterable))
