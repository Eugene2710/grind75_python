# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Recursive dfs:
        traverse down the tree and recurse to the left and right children, while keeping track of max node val in function call stack/its parent nodes
        -> if node.val >= max: res+=1

        time complexity: O(N)
        space complexity: O(N)
        """
        # there is always a root and root is counted as good node, hence default is 1
        res: int = 1
        max: int = root.val

        def dfs(curr: TreeNode, max: int) -> None:
            if curr is None:
                return None
            if curr.val >= max:
                nonlocal res
                res += 1
                max = curr.val
            if curr.left:
                dfs(curr.left, max)
            if curr.right:
                dfs(curr.right, max)

        dfs(root.left, max)
        dfs(root.right, max)
        return res

    """
    [3,1,4,3,null,1,5]
    function call stack
    [
        dfs(3.3)
        dfs(3.left, stack, max), line 31
    ]
    stack
    [
        3
    ]

    """
