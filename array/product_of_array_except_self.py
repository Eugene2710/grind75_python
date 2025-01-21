class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        approach: use 2 lists, one for elem before current index and one for elem after current index
        time complexity: O(2N) = O(N)
        space complexity: O(N)
        """
        length: int = len(nums)
        res: list(int) = [1]*length

        for i in range(1,length):
            res[i] = res[i-1]*nums[i-1]

        right: int = 1
        for i in range(length-1,-1,-1):
            res[i] = res[i]*right
            right = right*nums[i]

        return res

