class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # stack question: everytime there is a new parentehesis, add its corresponding parenthesis to the stack and the parentheses have to be matched and removed in that exact order

        """
        Approach: 
        Iterate through array
        if open brackets are read: add corresponding parenthesis to stack, 
        else if close brackets are read: 
            check if top of stack is the corresponding parenthesis
                if it is: 
                        remove from stack
                else:
                    return false
        (At the end of iteration through given array)
        if stack is empty:
            return true
        else:
            return false
        1) create stack
        
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        stack: str = []
        check: str = {")": "(", "]": "[", "}": "{"}

        for a in s:
            # if it is a closed bracket
            if a in check:
                # check if stack is not empty and top of parenthesis is a pair w current value in array
                if stack and stack[-1] == check[a]:
                    stack.pop()
                else:
                    return False
            # if it is an open bracket
            else:
                stack.append(a)

        return True if not stack else False