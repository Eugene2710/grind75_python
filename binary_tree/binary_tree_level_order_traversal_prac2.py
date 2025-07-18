from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Use a dequeue and bfs to assign nodes in that level to a list before appending the list to the nested list output

        time complexity: O(N)
        space complexity: O(N)
        """
        if root is None:
            return []
        dq: deque[TreeNode] = deque([root])
        res: list[list[int]] = []

        while dq:
            level_nodes: list[TreeNode] = []
            level_length: int = len(dq)
            for i in range(level_length):
               node: TreeNode = dq.popleft()
               level_nodes.append(node)

               if node.left:
                   dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level_nodes)

        return res




