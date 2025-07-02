# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        use a dfs/in-order traversal without appending the nodes to a result list to get the heights of left and right subtree
        keep track of the max diameter as a global variable, if node's left + right height > the global max diameter, it becomes the new global max diameter
        keep track of the node's height separately
        """
        self.diameter: int = 0
        def dfs(node) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left+right)
            return 1+max(left, right)

        dfs(root)
        return self.diameter