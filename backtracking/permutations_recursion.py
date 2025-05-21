class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        slice till only one elem left using recursion
        from one elem and add the next elem to the front and back of that elem
        time complexity: N! * 2(N)
        space complexity: N! * N
        """
        # base case: if len of nums is 0
        if len(nums) == 0:
            return [[]]
        # recurse from index 1 to the end of nums list
        perms: list[list[int]] = self.permute(nums[1:])
        res: list[int] = []
        #
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res