# 05
# Hard

# Maximum of Sliding Window: Given an array A and an integer K, find the maximum element in each 
# sliding window of size K. For example:

# A = [4,6,5,2,4,7] and K = 3, windows are as follows:

# [4,6,5,2,4,7] : Max = 6
# [4,6,5,2,4,7] : Max = 6
# [4,6,5,2,4,7] : Max = 5
# [4,6,5,2,4,7] : Max = 7

# Output: 6,6,5,7

# Hint: You can do this in O(n) time, by using the Queue with Max we implemented above


# -----------------------------------------------------

# Time Complexity:​ O(n)
# Space Complexity:​ O(k) - the queue with max will store up to K elements

from collections import deque

class SlidingWindowWithMax(object):
    def __init__(self, window_size: int):
        if window_size <= 0:
            raise Exception("Window size must be a positive integer")
        self.window_size = window_size
        self.q = deque()
        self.max_q = deque()

    def __repr__(self) -> str:
        return f"q={self.q} max_q={self.max_q}"

    def add(self, v: int) -> None:
        # trim vals outside window
        if len(self.q) == self.window_size:
            popped = self.q.popleft()
            if popped == self.max_q[0]:
                self.max_q.popleft()
        # add new vals
        self.q.append(v)
        while self.max_q and v > self.max_q[len(self.max_q)-1]:
            self.max_q.pop()
        self.max_q.append(v)
        
    def get_max(self) -> int:
        if not self.max_q:
            raise Exception("Could not get max, queue is empty")
        return self.max_q[0]

# -----------------------------------------------------

import pytest

def test_sliding_window_with_max():
    with pytest.raises(Exception):
        swwm = SlidingWindowWithMax(0)
    swwm = SlidingWindowWithMax(3)
    with pytest.raises(Exception):
        swwm.get_max()
    vals = [4,6,5,2,4,7]
    maxes = [4,6,6,6,5,7]
    for i in range(len(vals)):
        swwm.add(vals[i])
        assert(swwm.get_max() == maxes[i])

pytest.main()
