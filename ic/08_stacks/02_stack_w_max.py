# 02
# Easy

# Implement a Stack with a max() function. This function runs in O(1) time and returns the
# value of the maximum number on the stack


# -----------------------------------------------------

# Time Complexity: ​O(1) for push and pop
# Space Complexity:​ O(n) for n insertions

class StackWithMax(object):
    def __init__(self):
        self.s = []
        self.max_s = []

    def __repr__(self) -> str:
        return f"s={self.s} max_s={self.max_s}"

    def get_max(self) -> int:
        if self.max_s:
            return self.max_s[len(self.max_s)-1]
        return None

    def push(self, v: int) -> None:
        self.s.append(v)
        if not self.max_s or self.max_s[len(self.max_s)-1] <= v:
            self.max_s.append(v)

    def pop(self) -> int:
        if self.s:
            v = self.s.pop()
            if self.max_s[len(self.max_s)-1] == v:
                self.max_s.pop()
            return v
        return None
        

# -----------------------------------------------------

import pytest

def test_stack_w_max():
    swm = StackWithMax()
    assert(swm.get_max() == None)
    swm.push(3)
    assert(swm.get_max() == 3)
    swm.push(5)
    assert(swm.get_max() == 5)
    swm.push(2)
    # [3,5,2]
    assert(swm.get_max() == 5)
    assert(swm.pop() == 2)
    assert(swm.get_max() == 5)
    swm.push(5)
    swm.push(7)
    # [3,5,5,7]
    assert(swm.get_max() == 7)
    assert(swm.pop() == 7)
    assert(swm.get_max() == 5)
    assert(swm.pop() == 5)
    assert(swm.get_max() == 5)
    swm.push(2)
    # [3,5,2]
    assert(swm.get_max() == 5)
    assert(swm.pop() == 2)
    assert(swm.pop() == 5)
    assert(swm.get_max() == 3)

pytest.main()
