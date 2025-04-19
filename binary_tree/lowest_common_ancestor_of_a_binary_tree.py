# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        set 2 pointers: left to traverse down left side of tree, right to traverse right side of tree
        Possible cases:
        1. nodes are of different branches - result should be the parent of the nodes
            both left and right pointers point to p and q
        2. nodes are of the same branch - result should be either one of the nodes
            Bc both nodes have to be fo this branch, the first node that is found will be LCA
        """
        if not root:
            return None

        if root == p or root == q:
            return root

        left: TreeNode = self.lowestCommonAncestor(root.left, p, q)
        right: TreeNode = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

    """
    p=6, q=4 -> res=5
    l = self.lca(3.left,6,4)    r = self.lca(3.right,6,4)
    l = self.lca(5.left,6,4)    r = self.lca(5.right,6,4)
    5.left=p -> l = 6
    l = self.lca(2.left,6,4)    r = self.lca(2.right,6,4)
    l = self.lca(7.left,6,4)=None    r = self.lca(7.right,6,4)=None
    r = self.lca(2.right,6,4) -> r = 4
    """