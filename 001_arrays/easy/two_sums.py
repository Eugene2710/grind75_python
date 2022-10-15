"""
Approach
1) Create a list of res = [subtracted value from each value of array]
[7,2]
2)

1) Enumerate nums
2) Sort
2) 1 pointer at start, the opther at end

Assumption:
nums list is not sorted by default

Time Complexity: O(NlogN)
Space Complexity:O(N)
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        right = len(nums) - 1
        res = []
        left = 0

        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])

        while (left < right):
            if (target - nums[left][1]) == nums[right][1]:
                res.append(nums[left][0])
                res.append(nums[right][0])
                return res
            elif (target - nums[left][1] < nums[right][1]):
                right -= 1
            elif (target - nums[left][1] > nums[left][1]):
                left += 1