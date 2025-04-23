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

        # length: int = len(nums)
        # res: list[int] = [1]*length
        #
        # # get list with product of all elems in nums list to left of indexed elem
        # for i in range(1, length):
        #     res[i] = res[i-1]*nums[i-1]
        # # nums: list[int] = [1,2,3,4]   expected ans = [24, 12, 8, 6]
        # # res: list[int] = [1,1,2,6]
        #
        # left_product: int = 1
        # for i in range(length-1, -1, -1):
        #     res[i] *= left_product
        #     left_product *= nums[i]
        # return res
