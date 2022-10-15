# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: DFS recursion - first parameter to check if the left and right children are balanced, the second to count the number of children the node has

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        def dfs(root: 'Treenode') -> [bool, int]:
            # if node does not exist
            if not root:
                return [True, 0]

            # recursion dfs for left and right nodes
            left: [bool, int] = dfs(root.left)
            right: [bool, int] = dfs(root.right)

            # boolean value to check if the left and right children of current node is balanced
            # check if first index is true, and if left and right children has a difference of levels by less than 2
            balanced: bool = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]