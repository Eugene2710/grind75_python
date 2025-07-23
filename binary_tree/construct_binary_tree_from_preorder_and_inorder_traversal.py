# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Context: left of node in inorder is to the left branch, vice versa for right
        Approach:
        recursion with sliding window, .left recursion to curr node's left side in inorder & .right reursion to curr node's right side in order
        -> enum inorder and store them in an idx_map
        -> check if left > right, else: return None
        -> get curr val, its index in inorder, increment tracked index
        -> recurse to left of curr node and right of curr node in inorder by changing sliding windows accordingly

        Time complexity: O(N)
        Space complexity: O(N)
        """
        idx_map: dict[int, int] = {j:i for i,j in enumerate(inorder)}
        pre_idx: int = 0

        def slide(left: int, right: int) -> TreeNode | None:
            # termination case
            if left > right:
                return None

            nonlocal pre_idx
            curr_val: int = preorder[pre_idx]
            pre_idx += 1

            curr: TreeNode = TreeNode(curr_val)
            mid: int = idx_map[curr_val]

            curr.left = slide(left, mid-1)
            curr.right = slide(mid+1, right)
            return curr

        return slide(0, len(preorder)-1)

