# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        e.g. 4,2,7,1,3,0,3,6,9
        if null,

        Approach: DFS Recusion using temp node - assign left child to temp, assign right child to left child, assign temp to right child, recursion for left child and right child respectively.

        Time Complexity: O(N)
        Sapce Complexity: O(1)
        """

        # check if node is null
        if root == None:
            return None

        temp: Optional[TreeNode] = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root