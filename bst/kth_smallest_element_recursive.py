class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        traverse to extreme left using in-order traversal and traverse up from there
        time complexity: O(K)
        sapce complexity: O(K) - reciursion stack
        """
        def in_order_traversal(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            in_order_traversal(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            in_order_traversal(node.right)
        self.k: int = k
        self.res: int = 0
        in_order_traversal(root)
        return self.res


