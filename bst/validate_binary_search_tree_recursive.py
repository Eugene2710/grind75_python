class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], lower: Optional[TreeNode]=None, upper: Optional[TreeNode]=None) -> bool:
            if node is None:
                return True
            if lower is not None and node.val <= lower.val:
                return False
            if upper is not None and node.val >= upper.val:
                return False
            if not validate(node.left, lower, node):
                return False
            if not validate(node.right, node, upper):
                return False
            return True

        return validate(root, None, None)