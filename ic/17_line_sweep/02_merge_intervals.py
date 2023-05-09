# 02
# Medium

# Given a list of intervals, merge all overlapping intervals. 
# At the end of the merge, there should be no overlapping intervals.

# For example:
# Input = (1,3), (3,5), (6,8), (7,9)
# Output = (1,5), (6,9)


# -----------------------------------------------------

# Time Complexity: O(nlogn) - this time is taken to sort the points
# Space Complexity: O(n) - used on the points array

class Point(object):
    def __init__(self, val: int, is_low: bool):
        self.val = val
        self.is_low = is_low

    def __repr__(self) -> str:
        return f"{self.val}"

    def __eq__(self, other) -> bool:
        if self.val == other.val and self.is_low == other.is_low:
            return True
        return False

    def __gt__(self, other) -> bool:
        if self.__eq__(other):
            return False
        if self.val > other.val or (self.val == other.val and not self.is_low and other.is_low):
            return True
        return False
    
def merge_intervals(intervals: list) -> list:
    points = []
    for ivl in intervals:
        points.append(Point(ivl[0], True))
        points.append(Point(ivl[1], False))
    points = sorted(points)
    intervals = []
    open_intervals = 0
    curr_low = None
    for p in points:
        if p.is_low:
            if open_intervals == 0:
                curr_low = p.val
            else:
                pass
            open_intervals += 1
        else:
            open_intervals -= 1
            if open_intervals == 0:
                intervals.append((curr_low, p.val))
    return intervals            

# -----------------------------------------------------

import pytest

def test_merge_intervals():
    in1 = [(1,3), (3,5), (6,8), (7,9)]
    out1 = [(1,5), (6,9)]
    assert(merge_intervals(in1) == out1)

    in2 = [(1,3), (4,5), (6,8), (7,9)]
    out2 = [(1,3), (4,5), (6,9)]
    assert(merge_intervals(in2) == out2)

    in3 = [(14,20), (1,3), (7,8), (13,15), (6,9), (3,5), (7,11)]
    out3 = [(1, 5), (6, 11), (13, 20)]
    assert(merge_intervals(in3) == out3)

pytest.main()
