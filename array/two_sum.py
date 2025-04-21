"""
note:
- whenever index is required, use enumerate

Approach:
- dictionary with input array value as key, value as index (this allows index to be returned by searching for the key
- iterate through input arr and enumerate it
- if diff of each input value exists in dictionary, return value of key in dictionary and enumerated index of current input value
else, insert curr input value as key and enumerated index as value into dictionary
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        use a dict to store difference between target and indexed value as key, index of value as value
        enumerate input array and check if diff exits in key of dict

        time complexity: O(N)
        space complexity: O(2N)
        """
        mappedArr: dict[int, int] = {}
        for i, n in enumerate(nums):
            diff: int = target-n
            if diff in mappedArr:
                return [mappedArr[diff], i]
            mappedArr[n] = i



