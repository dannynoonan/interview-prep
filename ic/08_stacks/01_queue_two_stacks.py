# 01
# Medium

# Implement a Queue using 2 stacks.


# -----------------------------------------------------

# Time Complexity: Enqueue: O(1), Dequeue: O(n) in the worst case, O(1) amortized
# Space Complexity: O(1) extra space

class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, v: str) -> None:
        self.s1.append(v)

    def dequeue(self) -> str:
        if not self.s2:
            if not self.s1:
                return None
            while self.s1:
                v = self.s1.pop()
                self.s2.append(v)
        return self.s2.pop()


# -----------------------------------------------------

import pytest

def test_queue():
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    assert(q.dequeue() == 'A')
    q.enqueue('D')
    assert(q.dequeue() == 'B')
    assert(q.dequeue() == 'C')
    assert(q.dequeue() == 'D')
    assert(q.dequeue() == None)

pytest.main()
