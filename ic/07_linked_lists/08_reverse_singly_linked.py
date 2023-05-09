# 08
# Easy

# Reverse a singly-linked list. You should use O(1) space.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

class Node(object):
    def __init__(self, data: str):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList(object):
    def __init__(self, arr: list = []):
        if not arr:
            self.head = None
            self.tail = None
        else:
            for v in arr:
                self.append(v)

    def __repr__(self) -> str:
        out = ""
        n = self.head
        while n:
            out = f"{out}{n}"
            if n.next:
                out = f"{out}->"
            n = n.next
        return out
    
    def append(self, n: Node) -> None:
        if self.head:
            n.next = self.head
            self.head = n
        else:
            self.head = n
            self.tail = n

    def reverse(self) -> None:
        prev = None
        curr = self.head
        tail = curr
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.head = prev
        self.tail = tail

# -----------------------------------------------------

ll = LinkedList([1,2,3,4,5])
ll.reverse()





