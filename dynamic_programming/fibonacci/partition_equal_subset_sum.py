class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        DP, bottom up
        Iterate through each elem in nums, nested iteration each summed elem list
        and check if elem in summed list == target or elem+summed elem in summed list == target

        time complexity: O(N * sum(nums))
        space complexity:

        example input: [1,5,11,5] | [2,3,3, 1, 2, 5]
        target = 11
        i=0: sums = [0], dpSums = [0,5], sums = [0,5]
        i=1: sums = [0,5], dpSums = [0, 11, 16], sums = [0, 11, 16]
        """
        # check if sum of nums is odd or even number
        if sum(nums) % 2:
            return False

        # intialise a set and add zero as the first value
        sums: set[int] = set()
        sums.add(0) # why
        target: int = sum(nums)/2

        # traverse backwards and check for , forwards work too
        for i in range(len(nums)-1, -1, -1):
            dpSums: set[int] = set()
            for t in sums:
                if t == target or t+nums[i] == target:
                    return True
                dpSums.add(t)
                dpSums.add(t+sums[i])
            sums = dpSums
        return False

