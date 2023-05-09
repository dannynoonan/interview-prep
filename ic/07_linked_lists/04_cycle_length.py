# 04
# Medium

# Given a linked list that has a cycle, find the length of the cycle. The length is in
# number of nodes.


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

    def has_cycle(self) -> bool:
        slow = self.head
        fast = self.head
        while fast:
            fast = fast.next
            if fast == slow:
                return True
            if fast:
                fast = fast.next
                slow = slow.next
        return False

    def cycle_len(self) -> int:
        if not self.has_cycle():
            return 0
        slow = self.head
        fast = self.head
        while fast:
            fast = fast.next
            if fast == slow:
                break
            if fast:
                fast = fast.next
                slow = slow.next
        l = 1
        fast = fast.next
        while fast != slow:
            l += 1
            fast = fast.next
        return l

# -----------------------------------------------------

import pytest

def test_cycle_len():
    ll1 = LinkedList([1,2,3,4,5,6])
    ll1.tail.next = ll1.head.next.next.next
    assert(ll1.cycle_len() == 3)
    ll2 = LinkedList([1,2,3,4,5,6])
    ll2.tail.next = ll2.head.next.next
    assert(ll2.cycle_len() == 4)

pytest.main()
