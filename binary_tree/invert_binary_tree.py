# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time complexity: O(N)
# space complexity: O(1)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # swap the children
        tmp: TreeNode = root.left
        root.left: TreeNode = root.right
        root.right: TreeNode = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root