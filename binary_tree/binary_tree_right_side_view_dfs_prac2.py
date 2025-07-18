from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        dfs recursion approach: .right first followed by .left
        """
        if root is None:
            return []
        res: list[int] = []
        depth: int = 0
        def dfs(node: TreeNode | None, depth: int) -> None:
            # base case
            if node is None:
                return
            if len(res) == depth:
                res.append(node.val)

            self.dfs(node.right, depth+1)
            self.dfs(node.left, depth+1)

        dfs(root, depth)
        return res

