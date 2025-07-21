class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        bottom up approach - iterate through list with two pointers to
        -> check for 2 possible cases:
        a. rob house: use the prev pointer and add the curr house's val to it,
        b. don't rob: use the curr pointer
        -> check max between both and recalculate/reassign max
        -> move 2 pointers to right

        time complexity: O(N)
        space complexity: O(1)
        """
        prev: int = 0
        curr: int = 0

        for amt in nums:
            res: int = max(prev+amt, curr)
            prev = curr
            curr = res

        return res