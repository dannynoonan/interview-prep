# 04
# Hard

# Implement a Queue with O(1) lookup of the Maximum element


# -----------------------------------------------------

# Time Complexity:
# Insertion: O(n) worse case, O(1) amortized because we remove at most N elements for N insertions.
# Deletion and Max lookup: O(1)
# Space Complexity: O(n) on the Max queue

from collections import deque

class QueueWithMax(object):
    def __init__(self):
        self.q = deque()
        self.max_q = deque()

    def __repr__(self) -> str:
        return f"q={self.q} max_q={self.max_q}"

    def insert(self, v: int) -> None:
        self.q.append(v)
        while self.max_q and self.max_q[len(self.max_q)-1] <= v:
            self.max_q.pop()
        self.max_q.append(v)

    def delete(self) -> int:
        if not self.q:
            raise Exception("Queue is empty, nothing to delete")
        v = self.q.popleft()
        if self.max_q[0] == v:
            self.max_q.popleft()
        return v

    def get_max(self) -> int:
        if not self.q:
            raise Exception("Queue is empty, no max value")
        return self.max_q[0]

# -----------------------------------------------------

import pytest

def test_qwm():
    qwm = QueueWithMax()
    qwm.insert(4)
    qwm.insert(6)
    qwm.insert(2)
    assert(qwm.get_max() == 6)
    assert(qwm.delete() == 4)
    assert(qwm.get_max() == 6)
    assert(qwm.delete() == 6)
    assert(qwm.get_max() == 2)
    assert(qwm.delete() == 2)
    with pytest.raises(Exception):
        qwm.delete()

pytest.main()
