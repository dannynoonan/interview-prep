# 06
# Easy

# Check if a String is a rotation of another. 

# For example,
# ["canada", "dacana"] -> true
# ["canada", "canada"] -> true
# ["canada", "canary"] -> false
# ["dacana", "adacan"] -> true


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n)

def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    doubled_s1 = s1 + s1
    # if doubled_s1.__contains__(s2):
    if s2 in doubled_s1:
        return True
    return False

# -----------------------------------------------------

import pytest

def test_is_rotation():
    assert(is_rotation("canada", "dacana"))
    assert(is_rotation("canada", "canada"))
    assert(not is_rotation("canada", "canary"))
    assert(is_rotation("dacana", "adacan"))

pytest.main()
