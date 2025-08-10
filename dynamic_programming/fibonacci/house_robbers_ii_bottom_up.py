class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Similar approach to house robber 1, but separate case where first house to second last house are robbed and second house to last house are robbed
        DP bottom up approach: dp[i] = max(dp[i-1], dip[i-2]+nums[i])
        but with 2 pointers, one to retain the prev results which might not be added into dp[i-1]

        Boils down to 2 decisions which have  be made at every house represented by pointers and indexed value in list
        Since the prev pointed results are
        1. rob current house -> prev+nums[i]
        2. do not rob current house -> curr
        choose the max out of the 2 and iterate to next indexed val in list


        time complexity: O(N)
        space complexity: O(1)
        """
        n: int = len(nums)
        # base case 1: if there is only one elem in list
        if n == 1:
            return nums[0]
        # base case 2: if there are 2 elems in list
        if n == 2:
            return max(nums[0], nums[1])

        # case 3
        def rob_linear(house: list[int]) -> int:
            prev: int = 0
            curr: int = 0
            for amt in house:
                res: int = max(prev+nums[i], curr)
                prev = curr
                curr = res
            return res

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))