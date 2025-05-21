class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        recursive dfs:
        base case - if index out of range, add subset into result, return
        case where nums[i] is included - append nums[i] to subset before dfs(i+1)
        case where nums[i] is not included - pop from subset before dfs(i+1)
        time complexity: 2^n
        space complexity: 2^n
        """
        res: list[list[int]] = []
        subset: list[int] = []

        def dfs(i: int) -> None:
            # base case:
            if i >= len(nums):
                res.append(subset.copy())
                return

            # case to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # case to not include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res