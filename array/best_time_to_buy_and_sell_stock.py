"""
approach:
- if input value is smaller than smallest value(keep track of smallest value as a var), replace smallest with curr
- keep track of largest profit as res, if curr val-smallest>res, replace res

prices = [7,1,5,3,6,4]
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit: int = 0
        lowest: int = prices[0]
        for i in prices:
            profit: int = i-lowest
            if profit > max_profit:
                max_profit=profit
            if i < lowest:
                lowest = i

        return max_profit

