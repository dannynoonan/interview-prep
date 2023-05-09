# 03
# Hard

# You are given a list of buildings that are part of a skyline. For each building, you
# are given the height, start and end points.

# For example, if a building has [height=5, start=1, end=4],
# it represents a building of height 5 from point 1 on a number line to point 4.


# -----------------------------------------------------

# Time Complexity: O(Nlog(N))
# Space Complexity: O(N)

import heapq

class Point(object):
    def __init__(self, x: int, y: int, is_left: bool = False):
        self.x = x
        self.y = y
        self.is_left = is_left
    
    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}] left={self.is_left}"

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y and self.is_left == other.is_left:
            return True
        return False

    def __gt__(self, other) -> bool:
        if self.x > other.x or (self.x == other.x and self.is_left and not other.is_left):
            # nothing about self.y?
            return True
        return False

class Block(object):
    def __init__(self, x0: int, x1: int, y: int):
        self.x0 = x0
        self.x1 = x1
        self.y = y

    def __repr__(self) -> str:
        return f"x0={self.x0} x1={self.x1} y={self.y}"

    def __eq__(self, other) -> bool:
        if self.x0 == other.x0 and self.x1 == other.x1 and self.y == other.y:
            return True
        return False
 
def draw_skyline(buildings: list) -> list:
    points = []
    for b in buildings:
        points.append(Point(b.x0, b.y, True))
        points.append(Point(b.x1, b.y, False))
    points = sorted(points)
    skyline = []
    active_block = None
    active_rooflines = []
    heapq.heapify(active_rooflines)
    for p in points:
        if p.is_left:
            if not active_rooflines or p.y > -active_rooflines[0]:
                if active_block:
                    active_block.x1 = p.x
                    skyline.append(active_block)
                active_block = Block(x0=p.x, x1=None, y=p.y)
            else:
                pass
            heapq.heappush(active_rooflines, -p.y)
        else:
            if p.y == -active_rooflines[0]:
                active_block.x1 = p.x
                skyline.append(active_block)
                heapq.heappop(active_rooflines)
                if active_rooflines:
                    active_block = Block(x0=p.x, x1=None, y=-active_rooflines[0])
                else:
                    active_block = None
            else:
                active_rooflines.remove(-p.y)
    return skyline
            
# -----------------------------------------------------

import pytest

def test_skyline():
    buildings1 = []
    buildings1.append(Block(x0=11, x1=19, y=21))
    buildings1.append(Block(x0=2, x1=5, y=20))
    buildings1.append(Block(x0=16, x1=21, y=17))
    buildings1.append(Block(x0=4, x1=10, y=16))
    buildings1.append(Block(x0=14, x1=18, y=14))
    buildings1.append(Block(x0=8, x1=12, y=9))
    skyline1 = []
    skyline1.append(Block(x0=2, x1=5, y=20))
    skyline1.append(Block(x0=5, x1=10, y=16))
    skyline1.append(Block(x0=10, x1=11, y=9))
    skyline1.append(Block(x0=11, x1=19, y=21))
    skyline1.append(Block(x0=19, x1=21, y=17))
    assert(draw_skyline(buildings1) == skyline1)

    buildings2 = []
    buildings2.append(Block(x0=11, x1=19, y=21))
    buildings2.append(Block(x0=2, x1=5, y=20))
    buildings2.append(Block(x0=16, x1=21, y=17))
    buildings2.append(Block(x0=4, x1=10, y=16))
    buildings2.append(Block(x0=14, x1=18, y=14))
    skyline2 = []
    skyline2.append(Block(x0=2, x1=5, y=20))
    skyline2.append(Block(x0=5, x1=10, y=16))
    skyline2.append(Block(x0=11, x1=19, y=21))
    skyline2.append(Block(x0=19, x1=21, y=17))
    assert(draw_skyline(buildings2) == skyline2)

pytest.main()
