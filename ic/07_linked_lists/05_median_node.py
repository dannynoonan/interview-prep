# 05

# Find the median node of a linked list. For example:

# 1 -> 2 -> 3 -> 4 -> 5      Median node is 3.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

class Node(object):
    def __init__(self, data: str):
        self.data = str(data)
        self.next = None

    def __repr__(self) -> str:
        return self.data

class LinkedList(object):
    def __init__(self, arr: str|None = None):
        self.head = None
        self.tail = None
        if arr:
            for v in arr:
                self.append(v)

    def __repr__(self) -> str:
        out = ''
        n = self.head
        while n:
            out = f"{out}{n}"
            if n.next:
                out = f"{out}->"
            n = n.next
        return out

    def append(self, data: str) -> None:
        n = Node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def median(self) -> int:
        slow = self.head
        fast = self.head
        while fast:
            if fast == self.tail:
                return slow.data
            fast = fast.next
            if fast == self.tail:
                return slow.data
            fast = fast.next
            slow = slow.next

import pytest

def test_median():
    ll1 = LinkedList([1,2,3,4,5])
    assert(ll1.median() == '3')
    ll2 = LinkedList([1,2,3,4,5,6])
    assert(ll2.median() == '3')
    ll3 = LinkedList([4,5,6,7,1,2,3])
    assert(ll3.median() == '7')

pytest.main()
