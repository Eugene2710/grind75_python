class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        Approach: 2 pointers- Check if value in centre(floor) of list is smaller or larger than the target. If value is smaller, move left pointer to center of index of current array. Esle, move right pointer.

        Time Complexity: O(logN)
        Space Complexity: O(1)

        note: Consider edge case of input: 2, target:2. This means that while condition has to be >= instead of >.
        """

        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            else:
                right = center - 1

        return -1
