# 02 
# Hard

# You are given an array of numbers. Find a number that occurs more than 1/K of the time.

# For example:
# A = [2,4,5,2,4,2,2,1,5] and K = 3, Result = 2, which occurs more than Length/3 times.
# B = [2,4,5,2,4,2,6,1,5] and K = 3, No result as there is no number occurring > Length/3 times.


# -----------------------------------------------------

# Time Complexity: O(n)
# The total number of deletions from the map can be N, hence deleting items from map takes 
# O(n) amortized time.
# Space Complexity: O(k), used on the map.

def plurality_search(arr: list, k: int) -> int:
    tallies = {}

    for v in arr:
        if v in tallies:
            tallies[v] += 1
        elif len(tallies) < k:
            tallies[v] = 1
        else:
            vals_to_delete = []
            for val, tal in tallies.items():
                tallies[val] -= 1
                if tallies[val] == 0:
                    vals_to_delete.append(val)
            for vtd in vals_to_delete:
                del tallies[vtd]
            if len(tallies) < k:
                tallies[v] = 1
        
    tallies = {k:0 for k,v in tallies.items()}

    for v in arr:
        if v in tallies:
            tallies[v] += 1
            if tallies[v] > len(arr)/k:
                return v

    raise Exception(f"No value in arr of length={len(arr)} reached plurality threshold={len(arr)/k} for k={k}, final tally map={tallies}")


# -----------------------------------------------------

# I really feel like this should be the answer, though maybe there's a big O reason that favors the original approach

def plurality_search_better(arr: list, k: int) -> int:
    vals_to_counts = {}
    for v in arr:
        if v not in vals_to_counts:
            vals_to_counts[v] = 0
        vals_to_counts[v] += 1

    sorted_vals = [(k,v) for k,v in sorted(vals_to_counts.items(), key=lambda x: x[1], reverse=True)]
    if sorted_vals[0][1] > len(arr) / k:
        return int(sorted_vals[0][0])
    raise Exception(f'No value occurred more than {k} times')


# -----------------------------------------------------

import pytest

def test_plurality_search():
    arr1 = [2,4,5,2,4,2,2,1,5]
    k1 = 3
    assert(plurality_search(arr1, k1) == 2)

    arr2 = [2,4,5,2,4,2,6,1,5]
    k2 = 3
    with pytest.raises(Exception):
        plurality_search(arr2, k2)

pytest.main()
