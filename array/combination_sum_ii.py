class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking + sorting,
        Sort input list, use dfs/backtracking to recurse through permutaions,
        check for repeated values using while loop

        time complexity: O(N + 2^N) - N is due to the copying, 2^N is due to the decision tree/recursion
        space complexity: O(N)
        """
        res: list[list[int]] = []
        candidates.sort()
        length: int = len(candidates)

        def dfs(i: int, curr: list[int], total: int) -> None:
            # case 1: when sum==target
            if total == target:
                res.append(curr.copy())
                return
            # case 2: when sum > target or i >= length
            if total > target or i == length:
                return
            # case 3a: when sum<target, and
            curr.append(candidates[i])
            dfs(i=i + 1, curr=curr, total=total + candidates[i])
            curr.pop()
            # to prevent iterating through the same number
            while i + 1 < length and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i=i + 1, curr=curr, total=total)

        dfs(i=0, curr=[], total=0)
        return res
