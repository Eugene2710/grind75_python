from collections import deque
from typing import Deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """
        base case: if not root, return empty list
        iterate through nodes in each level,
        add .right followed by .left of each node into queue & add first node val into res list
        time complexity: O(N)
        space complexity: O(N)
        """
        # base case
        if root is None:
            return []
        queue: Deque[TreeNode] = deque([root])
        res: list[int] = []

        while queue:
            # track size of level to make sure each node is iterated through
            level_size: int = len(queue)
            for i in range(level_size):
                node: TreeNode = queue.popleft()
                if i == 0:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                # note: condition should be if instead of elif - all nodes in that level have to be appended to queue
                if node.right:
                    queue.append(node.right)
        return res