# 03
# Easy

# Find if a given Linked List has a cycle


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList(object):
    def __init__(self, head: Node|None = None, tail: Node|None = None):
        self.head = head
        self.tail = tail

    def append(self, data: int) -> None:
        n = Node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def __repr__(self) -> str:
        out = ''
        n = self.head
        while n:
            out = f"{out}{n}"
            if n.next:
                out = f"{out}->"
            n = n.next
        return out

def arr_to_ll(arr: list) -> LinkedList:
    ll = LinkedList()
    for v in arr:
        ll.append(v)
    return ll

# -----------------------------------------------------

def detect_cycle(ll: LinkedList) -> bool:
    slow = ll.head
    fast = ll.head
    while fast:
        fast = fast.next
        if fast == slow:
            return True
        if fast:
            fast = fast.next
            slow = slow.next
    return False

# -----------------------------------------------------

import pytest

def test_detect_cycle():
    ll = arr_to_ll([1,2,3,4,5])
    assert(detect_cycle(ll) == False)
    ll.tail.next = ll.head.next.next
    assert(detect_cycle(ll) == True)

pytest.main()
