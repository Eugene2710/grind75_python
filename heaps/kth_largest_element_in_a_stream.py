import heapq


class KthLargest:
    """
    heapify nums list, heappop while length of heap > k in constructor
    heappush val into heap in add method, if length of heap > k, heappop

    time complexity: O(nlogn)
    space complexity: O(k)
    """
    def __init__(self, k: int, nums: List[int]):
        self.k: int = k
        self.largest: list[int] = nums
        heapq.heapify(self.largest)
        while len(self.largest) > k:
            heapq.heappop(self.largest)

    def add(self, val: int) -> int:
        heapq.heappush(self.largest, val)
        if len(self.largest) > k:
            heapq.heappop(self.largest)
        return self.largest[0]