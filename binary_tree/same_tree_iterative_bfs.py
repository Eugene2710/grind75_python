from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        level order traversal and check if node from p == q at each iteration using a deque

        time complexity: O(N)
        space complexity: O(N)
        """
        if p is None and q is None:
            return True
        if p is None and q is not None or p is not None and q is None:
            return False
        dq_p: deque[TreeNode] = deque([p])
        dq_q: deque[TreeNode] = deque([q])

        while dq_p and dq_q:
            curr_p: TreeNode = dq_p.popleft()
            curr_q: TreeNode = dq_q.popleft()
            if curr_p.val != curr_q.val:
                return False
            if (curr_p.left is None and curr_q.left is not None or curr_p.left is not None and curr_q.left is None) or (
                    curr_p.right is None and curr_q.right is not None or curr_p.right is not None and curr_q.right is None):
                return False
            if curr_p.left:
                dq_p.append(curr_p.left)
                dq_q.append(curr_q.left)
            if curr_p.right:
                dq_p.append(curr_p.right)
                dq_q.append(curr_q.right)
        return True
