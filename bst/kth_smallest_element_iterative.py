class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        traverse to extreme left using in-order traversal and traverse up from there
        time complexity: O(K)
        sapce complexity: O(K) - reciursion stack
        """
        stack: list[int] = []
        curr: Optional[TreeNode] = root
        n: int = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right