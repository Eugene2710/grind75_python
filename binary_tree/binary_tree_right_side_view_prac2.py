from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Using deque and BFS, for each level, append the right most node to the output list

        time complexity: O(N)
        space complexity: O(levels)
        """
        if root is None:
            return []
        dq: deque[TreeNode] = deque([root])
        res: list[int] = []

        while dq:
            level_length: int = len(dq)
            curr: TreeNode = dq.popleft()
            for i in range(level_length):
                if i == 0:
                    res.append(curr.val)
                if curr.right:
                    dq.append(curr.right)
                if curr.left:
                    dq.append(curr.left)
        return res


