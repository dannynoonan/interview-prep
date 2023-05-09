# 09
# Medium

# Is Palindrome: Given a Linked List, determine if it is a Palindrome. 
# For example, the following lists are palindromes:
# A -> B -> C -> B -> A
# A -> B -> B -> A
# K -> A -> Y -> A -> K
# R A C E C A R

# Note: Can you do it with O(N) time and O(1) space? (Hint: Reverse a part of the list)


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
    def __init__(self, arr: list):
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

def is_palindrome(ll: LinkedList) -> bool:
    slow = ll.head
    fast = ll.head
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    ll2 = LinkedList()
    ll2.head = slow
    ll2.reverse()
    n1 = ll.head
    n2 = ll2.head
    while n2:
        if n2.data != n1.data:
            return False
        else:
            n1 = n1.next
            n2 = n2.next
    return True

# -----------------------------------------------------

import pytest

def test_is_palindrome():
    ll1 = LinkedList(['A','B','C','D'])
    assert(is_palindrome(ll1) == False)

    ll2 = LinkedList(['A','B','B','A'])
    assert(is_palindrome(ll2) == True)

    ll3 = LinkedList(['A','B','C','B','A'])
    assert(is_palindrome(ll3) == True)

    ll4 = LinkedList(['A','A','B','B','A','A','A'])
    assert(is_palindrome(ll4) == False)

    ll5 = LinkedList(['R','A','C','E','C','A','R'])
    assert(is_palindrome(ll5) == True)

pytest.main()
