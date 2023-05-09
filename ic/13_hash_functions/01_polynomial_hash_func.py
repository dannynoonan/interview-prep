# 01
# Hard

# Polynomial Hash Function: Generate a good hash function for a String.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def hash_func(s: str) -> int:
    c = 31
    hash_val = 0

    for i in range(len(s)):
        hash_val = hash_val * c + ord(s[i])

    return hash_val


# -----------------------------------------------------

import pytest

def test_hash_func():
    assert(hash_func('word') == 3655434)
    assert(hash_func('x') == 120)
    assert(hash_func('i am me') == 94196882325)

pytest.main()
