class Solution:
    def climbStairs(self, n: int) -> int:
        """
        fibonacci DP: using one and two step variables,
        loop from bottom up to move the one and two step pointers upwards/leftwards
        return one

        time complexity: O(n-1) = O(n)
        space complexity: O(1)
        """
        one: int = 1
        two: int = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one