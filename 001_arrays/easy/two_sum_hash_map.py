"""
Approach
1) Create a HASHMAP
2) Iterate the given array and ENUMERATE it - value of array as index 0, position of array as index 1
3) Check if difference of target and current value of array matches with any value in hashmap
    if it does, return position of value, aka index 1 of value in hashmap, and current index in array
    else, append curr value and position into hashmap

Time Complexity: O(N)
Space Complexity: O(2N) = O(N)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap to store iterated values of array

        mappedArr = {}

        for i, n in enumerate(nums):
            diff: int = target - n
            if diff in mappedArr:
                return [mappedArr[diff], i]
            mappedArr[n] = i
        return