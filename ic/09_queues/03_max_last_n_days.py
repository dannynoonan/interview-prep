# 03
# Medium

# You are given stock prices and the corresponding day of each stock price.

# For example:
# (32, 1), (45, 1), (37,2), (42,3), ..

# Here, 32 is the price and 1 is the day of the price.

# Say you are given these prices as an input stream. You should provide a function for
# the user to input a stock price and day. Your system should be able to tell
# the maximum stock price in the last 3 days.


# -----------------------------------------------------

# Time Complexity:
# addPrice()​ - O(n) worst case, but O(1) amortized because we do N removals for N insertions
# findMax()​ - O(n) because we go through entire sliding window. Can reduce this to O(1) use a ​Queue with Max​, 
# covered in the next section.
# Space Complexity:​ O(n)

from collections import deque

class QueueWithMax(object):
    def __init__(self, range: int):
        self.range = range
        self.q = deque()

    def __repr__(self) -> str:
        return str(self.q)

    def add_price(self, price: float, day: int) -> None:
        print(f"adding price={price} day={day}")
        self.q.append((price, day))
        print(f"q={self.q}")
        while self.q and (day - self.q[0][1]) >= self.range:
            self.q.popleft()
            print(f"q={self.q} after popleft")

    def find_max(self) -> int:
        highest = 0
        if not self.q:
            return highest
        for i in range(len(self.q)):
            highest = max(highest, self.q[i][0])
        return highest

# -----------------------------------------------------

import pytest

def test_qwm():
    qwm = QueueWithMax(3)
    qwm.add_price(5,1)
    qwm.add_price(7,1)
    assert(qwm.find_max() == 7)
    qwm.add_price(6,2)
    qwm.add_price(4,3)
    assert(qwm.find_max() == 7)
    qwm.add_price(3,4)
    assert(qwm.find_max() == 6)
    qwm.add_price(2,5)
    assert(qwm.find_max() == 4)

pytest.main()
