def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative inorder traversal method + check if curr value is lesser than or equal to previous value
        Time Complexity: O(n)
        Space Complexity: O(log n)
        """
        stack: list[TreeNode] = []
        curr: TreeNode = root
        prev: TreeNode = None

        while curr or stack:
            # only time you add node to stack is when you traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop() #this has to be before the if conditon bc curr=curr.right might be none and prev is not None, causing and error in the if
            # curr value should always be larger than prev
            # bc this check starts from the parent of the extreme left subtree node
            if prev and curr.val <= prev.val:
                return False

            prev = curr
            curr = curr.right

        return True