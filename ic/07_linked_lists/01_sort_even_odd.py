# 01
# Easy

# Odd Even Linked List: Given a Linked List L, separate it into 2 Linked Lists. 
# One contains L's odd nodes and the other contains L's even nodes. For example:

# Input: Head -> 1 -> 2 -> 3 -> 4 -> 5

# Result 1: Head -> 1 -> 3 -> 5
# Result 2: Head -> 2 -> 4

# Note: Odd and Even here refer to the node's position, not value.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1) because we are rearranging the nodes

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

def sort_even_odd(ll: LinkedList) -> tuple[LinkedList, LinkedList]:
    evens = LinkedList()
    odds = LinkedList()
    n = ll.head
    while n:
        odds.append(n.data)
        n = n.next
        if n:
            evens.append(n.data)
            n = n.next
    return odds, evens

# -----------------------------------------------------

ll = arr_to_ll([1,2,3,4,5])
odds, evens = sort_even_odd(ll)
