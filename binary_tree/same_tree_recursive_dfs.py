# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        recursive dfs approach: recurse through right and left branches,
        -> check if q = p for each recursion

        time complexity: O(N)
        space complexity: O(N)
        """
        # base case: if p is None or q is None
        if p is None or q is None:
            return p is q # this returns True if both are None, and False if only either is None
        # case: if p is not None and q is not None
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)