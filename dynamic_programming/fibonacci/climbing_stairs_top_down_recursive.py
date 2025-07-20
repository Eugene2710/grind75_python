class Solution:
    def climbStairs(self, n: int) -> int:
        """
        e.g 4 steps: a -> b -> c

        1+1+1
        1+2
        2+1

                    3
                2
            1

        DP approach - top down:

        {} , []
        dp[0] = 1
        dp[1] = 1
        dp[2] = dp[1] + dp[0] = 2
        dp[3] = dp[2] + dp[1] = 3
        dp[4] = dp[3] + dp[2]

        dfs(0,3)

        time complexity: O(2N) = O(N)
        space complexity: O(N)
        """
        res: int = 0
        steps: list[int | None] = [None] * (n + 1)

        def dfs(curr) -> None:
            if steps[curr] is not None:
                return steps[curr]
                # base case
            if curr == 0 or curr == 1:
                return 1
            else:
                steps[curr] = dfs(curr - 1) + dfs(curr - 2)
                return steps[curr]

        return dfs(n)
        """
        n=4 -> return dfs(2)+dfs(3) 
        [
            dfs(1)=1
            dfs(2) -> dfs(1)+dfs(0), line 32 = 1+1 = 2
            dfs(3) -> dfs(2)+dfs(1), line 32 = 2+1 = 3
            dfs(3)+dfs(2), line 32 = 3
            dfs(4), line 35
        ]
        """


