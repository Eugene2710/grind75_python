class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        approach: 
        sort intervals nested list and append first list of intervals into res nested list
        iterate through intervals, if res[-1][1] >= intervals[i][0]: res[-1][1] = max(res[-1][1], intervals[i][1])
        else: append list from intervals into res
        """
        # sort intervals - this will sort the value of the first index from each list within the nested list
        intervals.sort()

        res: list[list[int]] = []

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res


