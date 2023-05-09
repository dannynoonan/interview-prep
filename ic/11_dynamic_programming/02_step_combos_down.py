# 02

# Top Down Approach using Tabulation 


# -----------------------------------------------------

# Time Complexity​: O(N * 3) = O(N)
# Space Complexity​: O(N)

def step_combos_down(num_steps: int) -> int:
    step_tabs = [0] * (num_steps + 1)
    step_tabs[0] = 1
    for i in range(len(step_tabs)):
        if i >= 1:
            step_tabs[i] += step_tabs[i-1]
        if i >= 3:
            step_tabs[i] += step_tabs[i-3]
        if i >= 5:
            step_tabs[i] += step_tabs[i-5]
    return step_tabs[len(step_tabs)-1]

# -----------------------------------------------------

import pytest

def test_tabulate_step_combos():
    assert(step_combos_down(2) == 1)
    assert(step_combos_down(6) == 8)
    assert(step_combos_down(8) == 19)
    assert(step_combos_down(10) == 47)

pytest.main()
