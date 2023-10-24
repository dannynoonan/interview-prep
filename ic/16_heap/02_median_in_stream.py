# 02
# Hard

# Online Median: Given a stream of integers, find their median. If an integer is added to the
# stream, you should be able to update the median quickly.

# For example,
# 3,2,1,4,5 -> Median = 3
# 5,6,3,7 -> Median = (5+6)/2 = 5.5


# -----------------------------------------------------

# Time Complexity: Insert: O(logn), Median Lookup: O(1)
# Space Complexity: O(n)

import heapq

class StreamWithMedian(object):
    def __init__(self):
        self.lt_arr = []
        self.gt_arr = []
        heapq.heapify(self.lt_arr)
        heapq.heapify(self.gt_arr)

    def __repr__(self) -> str:
        return f"lt_arr={self.lt_arr} gt_arr={self.gt_arr}"

    def add(self, v: int) -> None:
        if len(self.gt_arr) == 0:
            heapq.heappush(self.gt_arr, v)
        elif len(self.gt_arr) > len(self.lt_arr):
            if v > self.gt_arr[0]:
                m = heapq.heappushpop(self.gt_arr, v)
                heapq.heappush(self.lt_arr, -m)
            else:
                heapq.heappush(self.lt_arr, -v)
        else:
            if v > self.gt_arr[0]:
                heapq.heappush(self.gt_arr, v)
            else:
                m = heapq.heappushpop(self.lt_arr, -v)
                heapq.heappush(self.gt_arr, -m)

    def median(self) -> float:
        if len(self.gt_arr) == 0:
            raise Exception("List is empty, no median value")
        if len(self.gt_arr) > len(self.lt_arr):
            return self.gt_arr[0]
        return (self.gt_arr[0] - self.lt_arr[0]) / 2


# simpler approach without comparisons 10/24/23

class MedianFinder(object):
    def __init__(self):
        self.heap_gt = []
        heapq.heapify(self.heap_gt)
        self.heap_lt = []
        heapq.heapify(self.heap_lt)
        
    def get_median(self) -> int:
        if not self.heap_gt:
            raise Exception('median finder is empty, could not extract median value')
        if len(self.heap_gt) > len(self.heap_lt):
            return self.heap_gt[0]
        else:
            return (self.heap_gt[0] - self.heap_lt[0]) / 2

    def add(self, v: int) -> None:
        if not self.heap_gt:
            heapq.heappush(self.heap_gt, v)
        elif not self.heap_lt or len(self.heap_gt) > len(self.heap_lt):
            popped = heapq.heappushpop(self.heap_gt, v)
            heapq.heappush(self.heap_lt, -popped)
        else:
            popped = heapq.heappushpop(self.heap_lt, -v)
            heapq.heappush(self.heap_gt, -popped)
        
# -----------------------------------------------------

import pytest

def test_stream_w_median():
    swm = StreamWithMedian()
    with pytest.raises(Exception):
        swm.median()
    swm.add(5)
    swm.add(8)
    swm.add(2)
    assert(swm.median() == 5.0)
    swm.add(9)
    assert(swm.median() == 6.5)

pytest.main()
