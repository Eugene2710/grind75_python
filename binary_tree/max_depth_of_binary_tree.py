class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        - similar to diameter of binary tree qn - but global diameter is not required since ther is not a case where the
        diameter might be larger not at the root level
        recurse and add 1 to every recusion if .left/.right exists.
        check for max depth at end of every recursion
        """

        def dfs(node) -> int:
            if node is None:
                return 0
            left: int = dfs(node.left)
            right: int = dfs(node.right)
            return 1 + max(left, right)

        return dfs(root)

        # # Base case: if the node is None, the depth is 0
        # if not root:
        #     return 0
        # # Recursively find the maximum depth of the left and right subtrees,
        # # then add 1 for the current node.
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))