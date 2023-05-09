# 01
# Easy

# Implement a Queue using an array.


# -----------------------------------------------------

# Time Complexity: O(1) for insertion and deletion
# Space Complexity: O(1) extra space after the initial array

class Queue(object):
    def __init__(self, capacity):
        self.q = [None] * capacity
        self.curr_size = 0
        self.front_i = 0
        self.back_i = 0
        
    def __repr__(self):
        return str(self.q)
        
    def enqueue(self, val: int) -> None:
        if self.curr_size == len(self.q):
            raise Exception(f"can't append val={val}, queue is at capacity")
        self.q[self.back_i] = val
        self.curr_size += 1
        if self.back_i == len(self.q)-1:
            self.back_i = 0
        else:
            self.back_i += 1
            
    def dequeue(self) -> int:
        if self.curr_size == 0:
            raise Exception("can't remove from queue, queue is empty")
        val = self.q[self.front_i]
        self.curr_size -= 1
        if self.front_i == len(self.q)-1:
            self.front_i = 0
        else:
            self.front_i += 1
        return val


# class Queue(object):
#     def __init__(self, capacity: int):
#         self.arr = [None] * capacity
#         self.next_i = None
#         self.last_i = None

#     def __repr__(self) -> str:
#         return f"{self.arr} next_i={self.next_i} last_i={self.last_i}"

#     def enqueue(self, val: int) -> None:
#         if self.last_i is None:
#             self.next_i = 0
#             self.last_i = 0
#             self.arr[self.last_i] = val
#             return
#         proposed_last_i = self.last_i + 1
#         if proposed_last_i == len(self.arr):
#             proposed_last_i = 0
#         if proposed_last_i == self.next_i:
#             raise Exception(f"Queue is at capacity, cannot enqueue new value {val}")
#         self.last_i = proposed_last_i
#         self.arr[self.last_i] = val

#     def dequeue(self) -> int:
#         if self.next_i is None:
#             raise Exception("Queue is empty, no value to dequeue")
#         v = self.arr[self.next_i]
#         if v is None:
#             raise Exception("Queue is empty, no value to dequeue")
#         self.arr[self.next_i] = None
#         self.next_i += 1
#         if self.next_i == len(self.arr):
#             self.next_i = 0
#         return v

# -----------------------------------------------------

import pytest

def test_queue():
    q = Queue(5)
    with pytest.raises(Exception):
        q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert(q.dequeue() == 1)
    q.enqueue(4)
    assert(q.dequeue() == 2)
    q.enqueue(5)
    q.enqueue(6)
    assert(q.dequeue() == 3)
    q.enqueue(7)
    q.enqueue(8)
    with pytest.raises(Exception):
        q.enqueue(9)
    assert(q.dequeue() == 4)
    assert(q.dequeue() == 5)
    q.enqueue(10)
    assert(q.dequeue() == 6)
    assert(q.dequeue() == 7)
    assert(q.dequeue() == 8)
    assert(q.dequeue() == 10)
    with pytest.raises(Exception):
        q.dequeue()

pytest.main()
