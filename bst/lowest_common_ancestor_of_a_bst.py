class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Using principle of BST - nodes on leftsubtree smaller than root and vicer versa,
        while curr, if curr larger than p and q, traverse left. While curr smaller than p and q traverse right. Else, LCA

        time complexity: O(N)
        space complexity: O(N)
        """
        curr: 'TreeNode' = root

        while curr:
            if curr.val < p.val and curr.val > q.val:
                curr.right
            elif curr.val > p.val and curr.val >q.val:
                curr.left
            else:
                return curr