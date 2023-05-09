# 06
# Hard

# Implement a data structure for a Least Recently Used (LRU) cache.


# -----------------------------------------------------

# Time Complexity: O(1) for both reads and writes
# Space Complexity: O(n) where n is the amount of data in cache

class Node(object):
    def __init__(self, key: str, val: str):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"{self.key}:{self.val}"

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        out = ""
        n = self.head
        while n:
            out = f"{out}{n}"
            if n.next:
                out = f"{out}->"
            n = n.next
        return out

    def add_most_recent(self, n: Node) -> None:
        if not self.head:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def remove_least_recent(self) -> Node:
        if not self.tail:
            return None
        n = self.tail
        if self.tail == self.head:
            self.tail = None
            self.head = None
            return n
        self.tail = n.prev
        self.tail.next = None
        n.prev = None
        n.next = None
        return n

    def remove(self, n: Node) -> None:
        if n == self.head:
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif n == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            n.prev.next = n.next
            n.next.prev = n.prev
        n.prev = None
        n.next = None

    def bump_to_most_recent(self, n: Node) -> None:
        self.remove(n)
        self.add_most_recent(n)


class LRUCache(object):
    def __init__(self, capacity: int):
        self.map = {}
        self.ll = LinkedList()
        self.capacity = capacity

    def add_update(self, key: str, val: str) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = val
            self.ll.bump_to_most_recent(node)
        else:
            node = Node(key, val)
            self.map[key] = node
            if len(self.map) > self.capacity:
                lru = self.ll.remove_least_recent()
                del self.map[lru.key]
            self.ll.add_most_recent(node)

    def get(self, key: str) -> str|None:
        if key not in self.map:
            return None
        n = self.map[key]
        self.ll.bump_to_most_recent(n)
        return n.val


import pytest

def test_lru_cache():
    lru = LRUCache(5)
    lru.add_update('1', 'one')
    lru.add_update('2', 'two')
    lru.add_update('3', 'three')
    lru.add_update('4', 'four')
    lru.add_update('5', 'five')
    assert(lru.get('1') == 'one')
    lru.add_update('6', 'six')
    assert(lru.get('2') == None)
    lru.add_update('4', 'FORE')
    assert(lru.ll.head.val == 'FORE')

pytest.main()
