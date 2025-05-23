class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        backtracking dfs
        choose: whether to append ( or )
        explore: recurse with updated partial string
        undo: when function goes out of scope, undo to sibling branch

        base case: when string completes - len(part) == 2*n
        case: if open_used < n - recurse with (
        case: if close_used < open_used - recurse with )

        time complexity: Cn * n
        space complexity: 2n
        """
        res: list[str] = []

        def backtrack(part: str, open_used: int, close_used: int) -> None:
            # base case
            if len(res) == 2*n:
                res.append(part)
                return
            # case where opens are left
            if open_used < n:
                backtrack(part+"(", open_used+1, close_used)
            if close_used < open_used:
                backtrack(part+")", open_used, close_used+1)

        backtrack("",0,0)
        return res