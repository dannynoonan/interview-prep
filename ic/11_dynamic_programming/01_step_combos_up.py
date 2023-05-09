# 01

# Climbing Steps Problem

# Let’s say you have to climb N steps. You can jump 1 step, 3 steps or 5 steps at a time. How
# many ways are there to get to the top of the steps.

# Bottom Up Approach using Tabulation 


# -----------------------------------------------------

# Time Complexity​: O(N * 3) = O(N)
# Space Complexity​: O(N)

def tabulate_step_combos(num_steps: int) -> int:
    step_tabs = [0] * (num_steps + 1)
    step_tabs[0] = 1
    for i in range(num_steps):
        if i+1 < len(step_tabs):
            step_tabs[i+1] += step_tabs[i]
        if i+3 < len(step_tabs):
            step_tabs[i+3] += step_tabs[i]
        if i+5 < len(step_tabs):
            step_tabs[i+5] += step_tabs[i]
    return step_tabs[len(step_tabs)-1]

# -----------------------------------------------------

import pytest

def test_tabulate_step_combos():
    assert(tabulate_step_combos(2) == 1)
    assert(tabulate_step_combos(6) == 8)
    assert(tabulate_step_combos(8) == 19)
    assert(tabulate_step_combos(10) == 47)

pytest.main()
