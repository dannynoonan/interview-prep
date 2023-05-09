# 02
# Easy

# Given an array of integers A, find the sum of each sliding window of size K.

# Variation: Instead of an array, what if you were presented with a stream of numbers. A new number
# can be added anytime. You want to find the sum of the last K elements.

# Note: The above problem can be solved without a Queue as well - just maintain a sum with 2
# pointers. However, a queue is needed for the Variation problem. We use this problem to illustrate
# the sliding window concept


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(K), because we store at most K nodes in the queue

from collections import deque

class SlidingWindowWithSum(object):
    def __init__(self, window_size: int):
        self.q = deque()
        self.window_size = window_size
        self.window_sum = 0

    def __repr__(self) -> str:
        return f"q={self.q} win_size={self.window_size} win_sum={self.window_sum}"

    def add_val(self, v: int) -> None:
        if len(self.q) == self.window_size:
            popped = self.q.popleft()
            self.window_sum -= popped
        self.window_sum += v
        self.q.append(v)

# -----------------------------------------------------

import pytest

def test_sliding_window_w_sum():
    swws = SlidingWindowWithSum(3)
    swws.add_val(5)
    swws.add_val(3)
    assert(swws.window_sum == 8)
    swws.add_val(7)
    assert(swws.window_sum == 15)
    swws.add_val(2)
    assert(swws.window_sum == 12)
    swws.add_val(3)
    assert(swws.window_sum == 12)
    swws.add_val(1)
    assert(swws.window_sum == 6)

pytest.main()
