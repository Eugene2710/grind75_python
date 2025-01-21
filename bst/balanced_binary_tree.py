class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #     """
        #     Possible cases:
        #     1. root is null
        #     2. root is not null, node is None
        #     3. root is not null, node
        #             3
        #         2       6
        #       1  2     5  8
        #               4
        #             3
        #     node_height={}
        #     stack=[(3,False)]
        #     node=3  visited = False stack=[]
        #     stack = [(3,True),(6,False),(2,False)]

        #     node=2  visited=False stack=[(3,True),(6,False)
        #     stack = [(3,True),(6,False),(2,True)]
        #     stack = [(3,True),(6,False),(2,True),(None,False),]

        #     left_height={[None,0]}
        #     left_height={[None,0]}
        #     """
        def dfs(root) -> list[bool, int]:
            if root is None:
                return [True, 0]
            left: list[bool, int] = dfs(root.left)
            right: list[bool, int] = dfs(root.right)
            # check if previous instances of left child were balanced,
            # if previous instances of right child were balanced,
            # left and right height has a diff of <= 1
            balanced: bool = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

"""
TIL
- make use of the returned value, i.e you can use one of the indexed values of the returned value
- make use of and statements to check conditions, i.e check if previous checks were True and the current check was True using and statement
"""

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        approach:
        traverse to end of tree using inorder traversal and once the the node.left is None and node.right is None: 
        add 1 to height, keep track of curr_height = max(left_height, right_height)+1
        and if abs(left_height-right_height)>1: return False
        else continue
        """
        def dfs(root: TreeNode | None) -> list[bool, int]
            """
            return 2 values: first val to check if balanced or not, second val to ge the height of the node
            """
            if root.left is None and root.right is None:
                return [True,0]
            left: list[bool, int] = dfs(root.left)
            right: list[bool, int] = dfs(root.right)

            balanced: bool = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, max(left[1], right[1])+1]
        
        return dfs(root)[0]
            