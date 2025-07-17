class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        traverse down the tree and make use of bst concept
        Possible cases
        1. if node.val >= one of them and <= than the other: return node.val
        2. if node.val > both of them: traverse down left child
        3. if node.val < both of them: traverse down right child

        time complexity: O(N)
        space complexity: O(1)
        """
        curr: TreeNode = root
        while curr:
            if (p.val >= curr.val and q.val <= curr.val) or (p.val <= curr.val and q.val >= curr.val):
                return curr
            elif curr.val > p.val and curr.val >q.val:
                curr = curr.left
            else:
                curr = curr.right
