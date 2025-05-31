class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
                5
            5      2      1
          5 2 1.  5

        Fibonacci DP problem: use bottom up approach -
        form list of amount+1 (last index is amount) of each elem being amount+1 by default
        iterate from first elem to amount+1 elem: within each amount, iterate through each coin possibility
        if the amount is >= coin possibility: take smallest possibility of each amount index

        time complexity: O(amount * coins)
        space complexity: O(amount)
        """
        # set default amount to amount+1; amount can also be any other larger amount
        dp: list[int] = [amount+1] * (amount+1)
        # set first elem to have 0 value since it costs 0 coin to be 0 amount
        dp[0] = 0

        for amt in range(1, amount+1):
            for c in coins:
                if amt >= c:
                    dp[amt] = min(dp[amt], 1+dp[amt-c])
        # return dp[amount] only if it is not the default amount assigned in the first line
        return dp[amount] if dp[amount] != amount+1 else -1
