class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        approach: 
        sort the input array
        using nested loops, and three pointers, for each outer loop, use the two sum II appraoch to check if sum is >/</= target
        keep moving first pointer to right, and repeat
        time complexity: O(NlogN) + O(N^2) =

        nums = [-1,0,1,2,-1,-4]
        after sorting -> [-4,-1,-1,0,1,2]
        """
        nums.sort()
        res: list(list(int)) = []
        # traverse to the third last elem
        for i in range(len(nums)-2):
            # if current elem is same as previous, skip
            if i>0 and nums[i]==nums[i-1]:
                continue
            left: int = i+1
            right: int = len(nums)-1
            while left<right:
                total: int = nums[i]+nums[left]+nums[right]
                if total==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return res

        nums.sort()
        res: list[list[int]] = []
        total: int = 0
        # iterate to the third last element since there are 2 more pointers that will reach the last and second last
        for i in range(len(num)-2):
            # to skip duplicate elements earlier on
            if i>0 and nums[i] == nums[i-1]:
                continue
            left: int = i+1
            right: int = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left <  right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res
