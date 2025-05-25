class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        split into left sorted portion and right sorted portion
        for left sorted portion, move left pointer if nums[l] <= nums[mid] and target > nums[l] or target < nums[l] <= nums[mid]
            move right pointer other wise
        else, do the reverse for right sorted portion

        time complexity: O(logN)
        space complexity: O(1)
        """
        l: int = 0
        r: int = len(nums)-1

        while l<=r:
            mid: int = (l+r)//2
            # happy path: case when mid = target
            if nums[mid] == target:
                return mid
            # left sorted portion
            elif nums[l] <= nums[mid]:
                # 2 cases when when left boundary should be increased
                # 2nd is when  target < nums[l] < nums[mid] -> this means target is definitely on the right side
                if nums[mid] < target or nums[l] > target:
                    l = mid+1
                else:
                    r = mid-1
            # right sorted portion
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid-1
                else:
                    l = mid+1

        return -1