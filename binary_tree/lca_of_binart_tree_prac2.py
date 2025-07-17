from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        """
        Use dfs recursion on left and right branches -> if left and right: return root , else: return left or right

        time complexity: O(N)
        space complexity: O(1)
        """
        # termination condition 1: if node is None -> return None
        if root is None:
            return None
        # termination condition 2: if node is equal to either of the input node -> return the node
        if root.val == p.val or root.val == q.val:
            return root
        # if not, recurse and traverse down the branches
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # after finding the nodes
        if left and right:
            return root
        return left or right


