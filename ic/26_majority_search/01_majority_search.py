# 01
# Medium

# You are given an array of numbers. Find a number that occurs more than half the time.

# For example, 
# A => [4,2,3,4,4,5,4,4,5,4,4], Result is 4
# A => [2,4,6,6,3,6,7,9,5,3], There is no result because there is no majority


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def majority_search(arr: list) -> int:
    v = arr[0]
    occ = 1
    for i in range(len(arr)):
        if arr[i] == v:
            occ += 1
        else:
            occ -= 1
        if occ == 0:
            v = arr[i]
            occ = 1

    final_v = v
    tally = 0
    for v in arr:
        if final_v == v:
            tally += 1
        
    if tally > len(arr) / 2:
        return final_v
    raise Exception(f"Didn't work: found final_v={final_v} on first pass, but on second pass tally was only {tally}")

# -----------------------------------------------------

import pytest

def test_majority_search():
    assert(majority_search([4,2,3,4,4,5,4,4,5,4,4]) == 4)
    with pytest.raises(Exception):
        majority_search([2,4,6,6,3,6,7,9,5,3])

pytest.main()
