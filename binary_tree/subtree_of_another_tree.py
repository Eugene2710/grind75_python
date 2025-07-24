# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        dfs recursion through every child of root,
        -> at very child of root, check if the node is the same as subRoot
        -> if it is check if the subtree at that point of the child is the same as the subRoot
        -> recurse and check through left or right child

        time complexity: O(N*M)
        space complexity: O(N)
        """
        def isSame(main: TreeNode, sub: TreeNode) -> bool:
            if main is None or sub is None:
                return main is sub
            if main.val != sub.val:
                return False
            return isSame(main.left, sub.left) and isSame(main.right, sub.right)

        def dfs(node: TreeNode | None) -> bool:
            # base case: if node is None: return False
            if node is None:
                return False
            if node.val == subRoot.val and isSame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)