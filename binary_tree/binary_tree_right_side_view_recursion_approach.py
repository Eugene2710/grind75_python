from typing import Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            # base case
            if not node:
                return
            # append first node that is visited from the rightmost to result - first visit is the length of result
            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return result
