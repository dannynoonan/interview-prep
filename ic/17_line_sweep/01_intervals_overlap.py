# 01
# Medium

# Given a list of time intervals, find if any of them overlap.

# For example,
# Intervals -> [5,7], [1,3], [6,9] -> Intervals [5,7] and [6,9] overlap, so we return true


# -----------------------------------------------------

# Time Complexity: O(NlogN), where N is the number of intervals. NlogN time is for sorting the Points.
# Space Complexity: O(N)


# tuple / itemgetter approach

from operator import itemgetter

def intervals_overlap(intervals: list) -> bool:
    points = []
    for intvl in intervals:
        points.append((intvl[0], True))
        points.append((intvl[1], False))
    points = sorted(points, key=itemgetter(0, 1))

    intvl_open = False
    for p in points:
        if p[1]:
            if intvl_open:
                return True
            intvl_open = True
        else:
            intvl_open = False

    return False


# dict / itemgetter approach

def intervals_overlap_dict(intervals: list) -> bool:
    points = []
    for intv in intervals:
        points.append(dict(x=intv[0], start=True))
        points.append(dict(x=intv[1], start=False))
    sorted_points = sorted(points, key=itemgetter('x', 'start'))

    intv_open = False
    for p in sorted_points:
        if p['start'] and intv_open:
            return True
        if p['start']:
            intv_open = True
        else:
            intv_open = False
        
    return False


# OO solution using explicit object comparison

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
        if self.val > other.val or (self.val == other.val and self.is_low and not other.is_low):
            return True
        return False

def intervals_overlap_oo(intervals: list) -> bool:
    points = []
    for ivl in intervals:
        points.append(Point(ivl[0], True))
        points.append(Point(ivl[1], False))
    points = sorted(points)
    open_interval = False
    for p in points:
        if p.is_low:
            if open_interval:
                return True
            else:
                open_interval = True
        else:
            open_interval = False
    return False

# -----------------------------------------------------

import pytest

def test_intervals_overlap():
    assert(not intervals_overlap([[1,3], [6,9]]))
    assert(intervals_overlap([[5,7], [1,3], [6,9]]))
    assert(not intervals_overlap([[5,7], [10,13], [1,3], [7,8]]))
    assert(not intervals_overlap([[3,6], [1,3], [6,9]]))
    assert(intervals_overlap([[6,8], [1,5], [2,4]]))

    assert(not intervals_overlap_dict([[1,3], [6,9]]))
    assert(intervals_overlap_dict([[5,7], [1,3], [6,9]]))
    assert(not intervals_overlap_dict([[5,7], [10,13], [1,3], [7,8]]))
    assert(not intervals_overlap_dict([[3,6], [1,3], [6,9]]))
    assert(intervals_overlap_dict([[6,8], [1,5], [2,4]]))

    assert(not intervals_overlap_oo([[1,3], [6,9]]))
    assert(intervals_overlap_oo([[5,7], [1,3], [6,9]]))
    assert(not intervals_overlap_oo([[5,7], [10,13], [1,3], [7,8]]))
    assert(not intervals_overlap_oo([[3,6], [1,3], [6,9]]))
    assert(intervals_overlap_oo([[6,8], [1,5], [2,4]]))

pytest.main()
