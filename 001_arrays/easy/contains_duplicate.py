"""
Approach
1) Create hashmap with key as value or set
2) Iterate through array and add value into set.
3) Check if value is in set fro every iteration.

Time Complexity: O(N)
Space complexity: O(N)

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()

        for i in nums:
            if i in numSet:
                return True
            numSet.add(i)

        return False