import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        append euclidean distances of each point(x^2 + y^2 will do), x and y coordinates to list
        heapify list, pop from list k times and append x and y coordinates into res list

        time complexity: O(klogn)
        space complexity: O(3n)
        """
        minHeap: list[list[int]] = []
        for x, y in points:
            sqr: int = x**2 + y**2
            minHeap.append([sqr, x, y])
        heapq.heapify(minHeap)
        res: list[list[int]] = []
        while k > 0:
            sqr, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
