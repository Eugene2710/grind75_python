import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        multiply elem in input stones list by -1 and store in list, heapify list (largest value are not smallest and vice versa)
        heappop 2 smallest elem, smallest elem - 2nd smallest elem, heappush res
        repeat while loop till len(heap)<=1

        time complexity: nlogn + n-1 = nlogn
        space complexity: n
        """
        input: list[int] = [-num for num in stones]
        heapq.heapify(input)

        while len(input) >= 2:
            a = heapq.heappop(input)
            b = heapq.heappop(input)
            if a - b != 0:
                heapq.heappush(input, a - b)

        return -input[0] if input else 0