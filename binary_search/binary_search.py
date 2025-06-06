class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Quick sort to sort through input to find target

        time complexity: O(log N)
        space complexity: O(1)
        """
        l: int = 0
        r: int = len(nums)-1
        while l <= r:
            mid: int = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1