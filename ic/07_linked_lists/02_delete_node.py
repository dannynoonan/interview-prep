# 02
# Medium

# Given a linked list and pointers to a node N and its previous node Prev, delete N from
# the linked list.


# -----------------------------------------------------

# Time Complexity: O(1)
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

def delete_node(ll: LinkedList, n: Node, prev: Node) -> None:
    if ll.head == n:
        ll.head = ll.head.next
    elif ll.tail == n:
        ll.tail = prev
    else:
        prev.next = n.next

# -----------------------------------------------------

ll1 = arr_to_ll([1,2,3,4,5])
prev1 = ll1.head.next
n1 = ll1.head.next.next
delete_node(ll1, n1, prev1)
# ll1 = 1->2->4->5

ll2 = arr_to_ll([1,2,3,4,5,6,7])
prev2 = ll2.head
n2 = prev2.next
delete_node(ll2, n2, prev2)
# ll2 = 1->3->4->5->6->7

ll3 = arr_to_ll([1,2,3,4,5])
prev3 = ll3.head.next.next.next
n3 = ll3.tail
delete_node(ll2, n3, prev3)
# ll3 = 1->2->3->4
