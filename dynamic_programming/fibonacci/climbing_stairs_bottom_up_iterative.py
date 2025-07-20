class Solution:
    def climbStairs(self, n: int) -> int:
        """
        e.g 4 steps: a -> b -> c

        1+1+1 +1
        1+1+2
        1+2 +1
        2+1 +1
        2+2
        bracktracking way/brute force: keep track of CURR_steps,
        backtrack(curr_steps, end) -> backtrack(0, 3) ->

        DP approach - bottom up: starting from last step go back 1 step at a time
        e.g at step 3 = take result from step 2 + 1 step OR take result from step 1 + 2 steps
            at step 2 = take result from step 1 + 2 steps OR take result from step 0 + 2 steps

        {} , []
        dp[0] = 1
        dp[1] = 1
        dp[2] = dp[1] + dp[0] = 2
        dp[3] = dp[2] + dp[1] = 3
        dp[4] = dp[3] + dp[2]

        time complexity: O(N)
        space complexity: O(N)
        """
        res: int = 0
        dp: list[int] = [0] * (n + 1)

        for i in range(
                n + 1):  # n=3 => i=0, dp[0]=1 -> i=1, dp[1] = 1 -> i=2, dp[2] = dp[1]+dp[0] = 1+1 = 2, dp[3] = dp[2]+dp[1] = 2+1 = 3
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]