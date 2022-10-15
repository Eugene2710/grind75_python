# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Approach: Using the principle of BST, if p and q are < curr value, traverse left. If p and q are > curr value, traverse right. Else, p and q are on separate sides of the tree and the LCA is the root node.

        Cases:
        1. p and q are on separte sides of tree - right and left
        2. p or q are not ancestors/descendants, but have common ancestors - when searching upwards
        3. p or q are ancestors/descendants
        """

        curr: 'Treenode' = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr