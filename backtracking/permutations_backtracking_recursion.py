class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking dfs recursion approach
        base case: termination condition - when all positions are fixed, append to res and return
        fix position, swap indexed elem and input elem in backtrack dfs recursion method, backtrack

        time complexity: O(N! * N)
        space complexity: O(N! * N)
        """
        res: list[list[int]] = []

        def backtrack(first: int) -> None:
            # base case: all positions fixed -> record one permutation
            if first == len(nums):
                res.append(nums[:]) # a faster way than nums.copy()
                return
            # try every choice for position 'first'
            for i in range(first, len(nums)):
                # swap item to pass into backtracking recursion with curr index in iteration
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)

        backtrack(0)
        return res