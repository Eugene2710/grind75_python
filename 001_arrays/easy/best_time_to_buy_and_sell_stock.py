"""
Approach:
1) Intialize 2 variables: min, maxProfit
2) Iterate through prices array. If elem < min, min=elem. maxProfit = max(elem-min, maxProfit )

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        res = 0

        for elem in prices:
            lowest = min(elem, lowest)
            res = max(elem - lowest, res)

        return res