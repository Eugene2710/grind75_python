class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        approach:
        traverse to end of tree using inorder traversal and once the the node.left is None and node.right is None: 
        add 1 to height, keep track of curr_height = max(left_height, right_height)+1
        and if abs(left_height-right_height)>1: return False
        else continue
        """
        if node is None:
            return True
        if lower
