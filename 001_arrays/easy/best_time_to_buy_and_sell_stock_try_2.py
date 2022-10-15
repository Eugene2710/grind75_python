class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach: Track lowest price and highest positive profit, iterate once through given array/list. Return highest positive profit.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        maxProfit: int = 0
        profit: int = 0
        lowestPrice: int = prices[0]

        for a in prices:
            if a < lowestPrice:
                lowestPrice = a
            if a - lowestPrice > 0:
                profit = a - lowestPrice
                if maxProfit < profit:
                    maxProfit = profit

        return maxProfit
