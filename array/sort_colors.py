class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Quick sort w partitioning
        iterate through input list, use 3 pointers - left, i, right
        Case 1: If i pointer points to 0, swap left and i, increment l and i.
        Case 2: If i pointer points to 1, increment i. (no swap)
        Case 3: If i pointer points to 2, swap right and i, decrement r.

        time complexity: O(N)
        space complexity: O(N)
        """
        l: int = 0
        r: int = len(nums)-1
        i: int = 0

        def swap(i: int, j: int) -> None:
            tmp: int = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(i=l, j=i)
                l += 1
            elif nums[i] == 2:
                swap(i=i, j=r)
                r -= 1
                i -= 1 # to prevent incrementing when nums[i]==2
            i += 1