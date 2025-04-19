# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List, Deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level order traversal of a binary tree and returns a list of levels,
        where each level is a list of node values at that depth.
        """
        if root is None:
            return []

        result: List[List[int]] = []
        queue: Deque[TreeNode] = deque([root])

        while queue:
            level_size: int = len(queue)
            level_nodes: List[int] = []

            for _ in range(level_size):
                node: TreeNode = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result
    """
    input = [3,9,20,null,null,15,7]
    queue = [3], level_size = 1, node=3 queue=[], level_nodes=[3], queue=[9,20], res=[[3]]
    level_size=2, level_nodes=[], node=9 queue=[20], level_nodes=[9], node=20 queue=[], level_nodes=[9,20], queue=[15], queue=[15,7]
    
    TIL
    - resetting of variables in each while loop
    - 
    """
